const chatWindow = document.getElementById('chatWindow');
const chatForm = document.getElementById('chatForm');
const chatInput = document.getElementById('chatInput');
const suggestionBox = document.getElementById('suggestionBox');

function getCSRFToken() {
  const input = document.querySelector('[name=csrfmiddlewaretoken]');
  return input ? input.value : '';
}

function appendMessage(text, type) {
  const div = document.createElement('div');
  div.className = `${type}-message message`;
  div.textContent = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function updateSuggestion(data) {
  const category = data.category || 'Not identified';
  const priority = data.priority || 'N/A';
  const query = new URLSearchParams();
  if (data.category && !['Track Complaint', 'General Complaint Guidance'].includes(data.category)) query.set('category', data.category);
  if (data.priority) query.set('priority', data.priority);
  const submitUrl = query.toString() ? `${window.submitComplaintUrl}?${query.toString()}` : window.submitComplaintUrl;
  const steps = (data.steps || []).map(step => `<li>${step}</li>`).join('');
  suggestionBox.innerHTML = `
    <h3>Suggested Category: ${category}</h3>
    <p><strong>Priority:</strong> ${priority}</p>
    ${steps ? `<ol>${steps}</ol>` : ''}
    <a class="btn btn-primary small-btn" href="${submitUrl}">Use in Complaint Form</a>
  `;
}

async function sendMessage(message) {
  if (!message.trim()) return;
  appendMessage(message, 'user');
  chatInput.value = '';
  try {
    const formData = new FormData();
    formData.append('message', message);
    const response = await fetch(window.assistantReplyUrl, {
      method: 'POST',
      headers: { 'X-CSRFToken': getCSRFToken() },
      body: formData
    });
    const data = await response.json();
    appendMessage(data.reply, 'bot');
    updateSuggestion(data);
  } catch (error) {
    appendMessage('Sorry, the assistant could not respond. Please try again.', 'bot');
  }
}

if (chatForm) {
  chatForm.addEventListener('submit', (event) => {
    event.preventDefault();
    sendMessage(chatInput.value);
  });
}

document.querySelectorAll('.quick-actions button').forEach(button => {
  button.addEventListener('click', () => sendMessage(button.dataset.message));
});
