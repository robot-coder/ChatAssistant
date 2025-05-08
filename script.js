# Chat Assistant JavaScript

const sendMessage = async () => {
    const userInput = document.getElementById('user-input').value;
    const responseContainer = document.getElementById('messages');

    const response = await fetch('/chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    });

    const data = await response.json();
    responseContainer.innerHTML += `<div>User: ${userInput}</div>`;
    responseContainer.innerHTML += `<div>Assistant: ${data.response}</div>`;
    document.getElementById('user-input').value = '';
};

document.getElementById('send-button').addEventListener('click', sendMessage);
