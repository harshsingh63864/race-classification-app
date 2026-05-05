from flask import Flask, render_template, request, jsonify
import torch
import clip
from PIL import Image
import io
import base64
import json
from werkzeug.utils import secure_filename
import os
import socket

def find_available_port(start_port=5000, end_port=5010):
    """Find an available port"""
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    return None

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

import urllib.request

MODEL_PATH = "clip_lvm_model.pt"
if not os.path.exists(MODEL_PATH):
    print("⏳ Downloading model from GitHub Releases...")
    urllib.request.urlretrieve(
        "https://github.com/harshsingh63864/race-classification-app/releases/download/v1.0/clip_lvm_model.pt",
        MODEL_PATH
    )
    print("✅ Model downloaded!")

# Load model and features
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Load saved model checkpoint
checkpoint = torch.load(MODEL_PATH, map_location=device)  # ← changed 'clip_lvm_model.pt' to MODEL_PATH
text_features = checkpoint['text_features'].to(device)
class_names = checkpoint['class_names']

print(f"✅ Model loaded on {device}")
print(f"📁 Classes: {class_names}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read and process image
        image_data = file.read()
        image = Image.open(io.BytesIO(image_data)).convert('RGB')
        
        # Save uploaded image
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        
        # Preprocess and predict
        image_input = preprocess(image).unsqueeze(0).to(device)
        
        with torch.no_grad():
            image_features = model.encode_image(image_input)
            image_features /= image_features.norm(dim=-1, keepdim=True)
            
            # Compute similarity with text features
            similarity = image_features @ text_features.T
            probabilities = torch.softmax(similarity, dim=1)
            
            # Get prediction and confidence
            pred_idx = similarity.argmax(dim=1).item()
            confidence = probabilities[0][pred_idx].item() * 100
            
            # Get similarity scores for all classes
            similarities = similarity[0].cpu().numpy().tolist()
        
        # Prepare response
        predicted_label = class_names[pred_idx]
        
        # Convert image to base64 for display
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode()
        
        response = {
            'success': True,
            'predicted_label': predicted_label.capitalize(),
            'confidence': round(confidence, 2),
            'image': f'data:image/png;base64,{img_base64}',
            'filename': filename,
            'all_scores': {
                class_names[i].capitalize(): round(float(similarities[i]), 4) 
                for i in range(len(class_names))
            }
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(
        debug=False, 
        host='0.0.0.0', 
        port=port, 
        threaded=True
    )
