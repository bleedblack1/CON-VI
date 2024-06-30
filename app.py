from flask import Flask, render_template, request, jsonify
import cohere

app = Flask(__name__)

cohere_client = cohere.Client('pd86jZcQcaP4uRixWIzftLJ6eUqSqizHDqN2vHE5')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'response': 'Please enter a prompt.'})

    response = cohere_client.generate(
        model='command-medium-nightly',

        prompt=prompt,
        max_tokens=50
    )

    return jsonify({'response': response.generations[0].text})

if __name__ == '__main__':
    app.run(debug=True)
