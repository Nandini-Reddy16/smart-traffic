from flask import Flask, request, jsonify
from flask_cors import CORS

import os

# Import your traffic logic
from traffic import analyze_traffic

app = Flask(__name__)
CORS(app)   # Allow frontend to connect

@app.route('/')
def home():
    return "Server Running!"

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get uploaded image
        file = request.files['image']

        if not file:
            return jsonify({"result": "No file uploaded"})

        # Create uploads folder
        os.makedirs("uploads", exist_ok=True)

        # Save file
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        # 🔥 Call your traffic logic
        result = analyze_traffic()

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)