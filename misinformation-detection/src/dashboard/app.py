from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Sample data for demonstration purposes
data = {
    "content": [
        "This is a true statement.",
        "This is a false statement.",
        "Check out this misleading information!",
    ],
    "reliability_score": [0.95, 0.10, 0.30],
    "evidence": [
        "Verified by trusted source.",
        "Debunked by fact-checkers.",
        "No credible sources found.",
    ],
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/api/flagged-content', methods=['GET'])
def flagged_content():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)