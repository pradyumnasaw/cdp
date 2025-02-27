function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return;

    appendMessage('User', userInput);

    fetch('/ask/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question: userInput})
    })
    .then(response => response.json())
    .then(data => appendMessage('Bot', data.answer))
    .catch(error => appendMessage('Bot', 'Error retrieving answer.'));

    document.getElementById('user-input').value = '';
}

function appendMessage(sender, text) {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>${sender}:</strong> ${text}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
