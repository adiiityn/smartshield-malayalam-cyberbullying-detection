function openChat() {
  document.getElementById("chatbot").style.display = "flex";
}

function closeChat() {
  document.getElementById("chatbot").style.display = "none";
}


/* FEATURE INFO PANEL */

function showPanel(type) {

  const data = {
    ai: "AI powered Malayalam cyberbullying detection system.",
    voice: "Voice input is converted to Malayalam text and analyzed.",
    realtime: "Real-time deep learning prediction using BiLSTM.",
    accuracy: "Model trained using goodwords and badwords dataset.",
    admin: "Admin dashboard for monitoring detection logs.",
    future: "Future updates include image, audio and social media detection."
  };

  document.getElementById("panelContent").innerHTML =
  `<h3>${data[type]}</h3>`;

  document.getElementById("panel").style.display = "block";
}

function closePanel() {
  document.getElementById("panel").style.display = "none";
}



/* VOICE RECOGNITION */

function startVoice() {

  if (!('webkitSpeechRecognition' in window)) {
    alert("Voice recognition not supported in this browser");
    return;
  }

  const recog = new webkitSpeechRecognition();

  /* Malayalam language support */
  recog.lang = "ml-IN";

  recog.start();

  recog.onresult = (e) => {

    const speechText = e.results[0][0].transcript;

    document.getElementById("userInput").value = speechText;

    sendMessage();
  };

}



/* SEND MESSAGE */

function sendMessage() {

  let input = document.getElementById("userInput");

  let text = input.value.trim();

  if (!text) return;

  let box = document.getElementById("chat-box");

  /* USER MESSAGE */

  box.innerHTML += `<div class="user">${text}</div>`;

  box.scrollTop = box.scrollHeight;



  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: text })
  })


  .then(response => response.json())


  .then(data => {

    /* BOT RESPONSE */

    box.innerHTML +=
    `<div class="bot">
        ${data.result}<br>
        <small>${data.suggestion}</small>
     </div>`;


    /* CYBERBULLYING ALERT */

    if (data.result.includes("Cyberbullying")) {

      let warning = document.getElementById("warning");

      warning.style.display = "block";


      /* TURN SCREEN RED */

      document.body.style.background = "#7a0000";


      setTimeout(() => {

        warning.style.display = "none";

        document.body.style.background =
        "linear-gradient(135deg,#1f4037,#99f2c8)";

      }, 3000);

    }


    box.scrollTop = box.scrollHeight;

  });



  input.value = "";

}



/* ENTER KEY SEND */

document.addEventListener("DOMContentLoaded", function () {

  const input = document.getElementById("userInput");

  input.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

      sendMessage();

    }

  });

});
