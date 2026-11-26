
const socket = new WebSocket('ws://127.0.0.1:8000/ws');

const messages = document.querySelector('#messages');
const input = document.querySelector('#message-input');
const form = document.querySelector('#chat-form');
const status = document.querySelector('#status');
const sendButton = document.querySelector('#send-button');

socket.onopen = () => {
  status.textContent = 'Connected';
  status.style.color = '#4ade80';
  sendButton.disabled = false;
};

socket.onmessage = (event) => {
  displayMessage('Server: ' + event.data, 'received');
};

socket.onclose = () => {
  status.textContent = 'Disconnected';
  status.style.color = '#f87171';
  sendButton.disabled = true;
};

socket.onerror = () => {
  status.textContent = 'Connection error';
  sendButton.disabled = true;
};

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const message = input.value;

  if (message.trim() === '') {
    return;
  }

  if (socket.readyState === WebSocket.OPEN) {
    socket.send(message);
    displayMessage('You: ' + message, 'sent');
    input.value = '';
  }
});

function displayMessage (text, type) {
  const message = document.createElement('div');

  message.classList.add('message', type);
  message.textContent = text;

  messages.appendChild(message);
  messages.scrollTop = messages.scrollHeight;
}
