function getBotResponse(input) {
    fetch('http://127.0.0.1:5000/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => addMessage(data.response, 'bot'))
    .catch(error => console.error('Error:', error));
}
