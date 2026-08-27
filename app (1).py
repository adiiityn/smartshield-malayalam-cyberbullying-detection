from flask import Flask, render_template, request, jsonify
import numpy as np
import re
import pickle
import pandas as pd
import os

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ✅ Optional: disable GPU error (safe)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Optional AI contextual layer
try:
    from openai import OpenAI
    client = OpenAI(api_key="YOUR_API_KEY")
except:
    client = None


app = Flask(__name__, template_folder="templates", static_folder="static")

app.config["JSON_AS_ASCII"] = False

# Load ML model
model = load_model("cyberbullying_model.h5")

# ✅ Fix Keras warning (optional but clean)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

tokenizer = pickle.load(open("tokenizer.pkl", "rb"))

# -----------------------------
# ✅ FIXED: CSV loading (Malayalam safe)
# -----------------------------
bad_df = pd.read_csv("badword_dataset.csv", encoding="utf-8-sig")
bad_df = bad_df.fillna("")

MAX_LEN = 25


# -----------------------------
# TEXT CLEANING (Malayalam Safe)
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^\u0D00-\u0D7Fa-zA-Z0-9\s]", "", text)
    return text.strip()


# -----------------------------
# BADWORD MATCHING
# -----------------------------
def detect_badword(message):
    for word in bad_df["text"].values:
        if word and word in message:
            row = bad_df[bad_df["text"] == word]
            if not row.empty:
                return True, row["alternative"].values[0]
    return False, None


# -----------------------------
# CONTEXTUAL AI CHECK
# -----------------------------
def contextual_ai(text):

    if client is None:
        return "SAFE"

    try:
        prompt = f"""
Classify the message below.

Only respond with:
SAFE
or
CYBERBULLYING

Message:
{text}
"""
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        result = response.output_text.strip()
        return result

    except:
        return "SAFE"


# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# PREDICTION API
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message = clean_text(data["message"])

    bad, alt = detect_badword(message)

    seq = tokenizer.texts_to_sequences([message])
    pad = pad_sequences(seq, maxlen=MAX_LEN)

    pred = model.predict(pad)[0][0]
    confidence = float(pred)

    if bad or confidence < 0.40:
        result = "Cyberbullying ❌"
        suggestion = alt if alt else "Please use respectful language."

    elif confidence > 0.70:
        result = "Safe Language ✅"
        suggestion = "No harmful content detected."

    else:
        ai = contextual_ai(message)

        if "CYBERBULLYING" in ai:
            result = "Cyberbullying ❌"
            suggestion = "This message may harm others."
        else:
            result = "Safe Language ✅"
            suggestion = "No harmful content detected."

    return jsonify({
        "result": result,
        "confidence": round(confidence * 100, 2),
        "suggestion": suggestion
    }), 200


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
