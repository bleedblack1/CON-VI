function sendPrompt() {
    const promptInput = document.querySelector('.input-area input');
    const prompt = promptInput.value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
    })
    .then(response => response.json())
    .then(data => {
        const responseContainer = document.querySelector('.response-container');
        responseContainer.innerHTML = `<p>${data.response}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
