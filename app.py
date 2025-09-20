import os
import json
import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# --- Initialization ---
app = Flask(__name__)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow messages

# --- Load Model & Class Labels ---
try:
    model = load_model('model.h5')
    with open('class_indices.json', 'r') as f:
        class_indices = json.load(f)
        class_labels = {v: k for k, v in class_indices.items()}
    print("✅ Model and class labels loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model or class labels: {e}")
    model, class_labels = None, None


# --- Helper Function ---
def prepare_image(img):
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded = np.expand_dims(img_array, axis=0)
    return img_array_expanded / 255.0


# --- Routes ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if model is None or class_labels is None:
        return jsonify({'error': 'Model not loaded. Check server logs.'}), 500
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        prepared_image = prepare_image(img)
        prediction = model.predict(prepared_image)

        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_class_label = class_labels.get(int(predicted_class_index), "Unknown")
        confidence = float(np.max(prediction))

        return jsonify({
            'prediction': predicted_class_label,
            'confidence': f'{confidence:.2%}'
        })
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500


# --- Run the App ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)