# 🛡️ SmartShield — AI-Based Cyberbullying Detection for Malayalam Text

> An AI-powered Natural Language Processing (NLP) system designed to detect and classify cyberbullying in Malayalam text using Machine Learning and Deep Learning techniques.

## 📌 Project Overview

**SmartShield** is an AI-based cyberbullying detection system focused on the Malayalam language.

The project addresses the growing need for automated moderation of Malayalam content on social media and online platforms. It uses Natural Language Processing, Machine Learning, and Deep Learning techniques to analyze Malayalam text and identify potentially harmful or cyberbullying content.

The project includes the creation and preparation of a Malayalam text dataset and experimentation with different machine learning and transformer-based approaches for text classification.

---

## 🎯 Objectives

* Detect cyberbullying in Malayalam text.
* Classify text based on its cyberbullying characteristics.
* Develop an NLP-based solution for a relatively under-resourced language.
* Explore Machine Learning, Deep Learning, and Transformer-based approaches.
* Build a system that can support safer online communication.
* Evaluate different approaches for Malayalam text classification.

---

## 🧠 Technologies Used

### Programming & Development

* Python
* Google Colab
* Jupyter Notebook

### Machine Learning & NLP

* Scikit-learn
* TensorFlow
* Keras
* NLTK
* Indic NLP

### Models & Techniques

* TF-IDF
* Logistic Regression
* Deep Learning
* IndicBERT
* MuRIL
* XLM-R

---

## 📊 Dataset

A Malayalam cyberbullying text dataset was created and prepared specifically for this project.

The dataset was collected from publicly available Malayalam online content and manually processed and organized for use in cyberbullying detection experiments.

### Dataset Preparation

The workflow included:

1. Collecting Malayalam text data.
2. Cleaning and preprocessing the text.
3. Identifying relevant cyberbullying-related content.
4. Preparing labels for classification.
5. Splitting the dataset for model training and evaluation.
6. Applying NLP preprocessing techniques.

> **Note:** The repository does not include any private, sensitive, or unauthorized personal data.

---

## 🔬 Methodology

The overall workflow follows these stages:

```text
Malayalam Text
      ↓
Data Collection
      ↓
Data Cleaning & Preprocessing
      ↓
Text Representation
      ↓
Feature Extraction / Tokenization
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Cyberbullying Classification
```

---

## 🤖 Models

### 1. TF-IDF + Logistic Regression

A traditional Machine Learning approach was implemented using:

* TF-IDF vectorization
* Logistic Regression

This provides a baseline for comparing more advanced approaches.

### 2. Deep Learning

Deep learning techniques were explored to improve the ability of the system to learn contextual patterns from Malayalam text.

### 3. Transformer-Based Models

Transformer-based multilingual language models were explored for Malayalam text classification, including:

* **IndicBERT**
* **MuRIL**
* **XLM-R**

These models provide stronger contextual understanding compared with traditional bag-of-words approaches.

---

## 📈 Results

The model was evaluated on a test set of **1,421 samples** using accuracy, precision, recall, and F1-score.

### Classification Report

| ClassPrecisionRecallF1-ScoreSupport |          |          |                |           |
| ----------------------------------- | -------- | -------- | -------------- | --------- |
| 0                                   | 1.00     | 0.98     | 0.99           | 673       |
| 1                                   | 0.98     | 1.00     | 0.99           | 748       |
| **Overall Accuracy**                |          |          | **0.99 (99%)** | **1,421** |
| **Macro Average**                   | **0.99** | **0.99** | **0.99**       | **1,421** |
| **Weighted Average**                | **0.99** | **0.99** | **0.99**       | **1,421** |

### Performance Summary

* **Accuracy:** 99%
* **Macro F1-Score:** 99%
* **Weighted F1-Score:** 99%
* **Test Samples:** 1,421
* **Class 0 Samples:** 673
* **Class 1 Samples:** 748

The results indicate strong classification performance on the evaluated test dataset, with balanced precision and recall across both classes.

> **Note:** The exact model associated with these results should be specified based on the model evaluation performed in the notebook.

---

## 🚀 Google Colab

The complete experimental notebook is available here:

[**Open SmartShield in Google Colab**](https://colab.research.google.com/drive/1unIuSe7jMF2fC1BSjn_argdV9MgkmPEY?usp=sharing)

The notebook contains the data preprocessing, model training, evaluation, and experimentation workflow.⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/adiiityn/smartshield-malayalam-cyberbullying-detection.git
```

Navigate to the project:

```bash
cd smartshield-malayalam-cyberbullying-detection
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Alternatively, the project can be executed directly through Google Colab.

---

## 📁 Project Structure

```text
smartshield-malayalam-cyberbullying-detection/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── SmartShield.ipynb
│
├── dataset/
│   └── ...
│
├── models/
│   └── ...
│
└── src/
    └── ...
```

> The final folder structure may vary depending on the files included in the project.

---

## 👥 Team

### Project Team

* **Adityan P** — [GitHub Profile]()
* **Shamil Shiras A**— [GitHub Profile]()
* **Aman SV**— [GitHub Profile]()

---

## 🔮 Future Improvements

* Improve the size and diversity of the Malayalam cyberbullying dataset.
* Explore additional Malayalam-specific language models.
* Improve classification performance on ambiguous and code-mixed Malayalam text.
* Develop a real-time cyberbullying detection interface.
* Deploy the trained model as a web application or API.
* Extend the system to support additional Indic languages.

---

## 📚 Key Learning Outcomes

Through this project, we explored:

* Malayalam NLP
* Text preprocessing
* Dataset creation and preparation
* Feature extraction
* Machine Learning classification
* Deep Learning
* Transformer-based NLP models
* Model evaluation
* Working with low-resource languages
* Experimentation and comparative model analysis

---

## ⭐ Project Highlights

* 🇮🇳 Focused on **Malayalam**, an under-resourced language in NLP.
* 🤖 Combines **Machine Learning, Deep Learning, and Transformer-based approaches**.
* 🧠 Experiments with **IndicBERT, MuRIL, and XLM-R**.
* 📊 Includes comparative model evaluation.
* 🛡️ Focuses on improving safety in Malayalam online communication.

---

## 📄 License

This project is currently presented as a public portfolio and academic project.

No open-source license has been applied at this time.
