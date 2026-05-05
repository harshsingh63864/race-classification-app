# Race Classification Web Application

A Flask-based web application for classifying facial images by race using OpenAI's CLIP model.

## Features

✅ **User-Friendly Interface** - Modern, responsive web interface matching your PowerPoint design
✅ **Real-time Predictions** - Upload images and get instant race classifications
✅ **Confidence Scores** - See prediction confidence for all 4 race categories
✅ **Visual Feedback** - Image preview and results display with confidence bars
✅ **Responsive Design** - Works on desktop and mobile devices

## Project Structure

```
Project-final/
├── app.py                    # Flask application backend
├── clip_lvm_model.pt        # Pre-trained model checkpoint
├── RFW_dataset_...ipynb     # Jupyter notebook with training code
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html          # Web interface HTML/CSS/JavaScript
├── uploads/                # Directory for uploaded images (auto-created)
└── data/                   # Dataset directory
    ├── Dataset.csv
    └── [race folders with images]
```

## Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install flask torch torchvision clip pillow numpy scikit-learn werkzeug
pip install git+https://github.com/openai/CLIP.git
```

### Step 2: Verify Model File

Make sure `clip_lvm_model.pt` exists in the project root. This file contains:
- Text features for the 4 race categories
- Class names (African, Asian, Caucasian, Indian)

## Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Output:
```
WARNING in app.runpy: Trying to run body of protect file...
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Open your browser and navigate to `http://localhost:5000`

## How to Use

1. **Upload Image**: Click "📁 Choose File" and select a facial image (JPG, PNG, etc.)
2. **Preview**: The image preview will appear below the upload button
3. **Predict**: Click "🚀 Predict" to classify the image
4. **View Results**: See the predicted race category and confidence score
5. **Compare Scores**: View all classification scores in the table

## Model Information

- **Model**: OpenAI CLIP (ViT-B/32)
- **Classes**: African, Asian, Caucasian, Indian
- **Training Accuracy**: ~90.58%
- **Approach**: Zero-shot learning with text-image similarity
- **Text Prompts**: "a photo of a [race] person"

## API Endpoints

### GET /
- Returns the main web interface

### POST /predict
- **Input**: Form data with file upload
- **Output**: JSON with prediction results

Example response:
```json
{
  "success": true,
  "predicted_label": "African",
  "confidence": 98.07,
  "image": "data:image/png;base64,...",
  "filename": "image.jpg",
  "all_scores": {
    "African": 0.9807,
    "Asian": 0.0089,
    "Caucasian": 0.0087,
    "Indian": 0.0017
  }
}
```

## Important Notices

⚠️ **Ethical Considerations**: This model is for educational and research purposes only. Use responsibly.

⚠️ **Limitations**: The model may have biases and limitations in accuracy across different populations.

⚠️ **Privacy**: Uploaded images are stored temporarily in the `uploads/` folder.

## Troubleshooting

### Port Already in Use
Change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to another port
```

### CUDA/GPU Issues
The app automatically uses GPU if available, falls back to CPU:
```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

### Model Not Found
Ensure `clip_lvm_model.pt` is in the same directory as `app.py`

### Import Errors
Reinstall CLIP from GitHub:
```bash
pip install --upgrade git+https://github.com/openai/CLIP.git
```

## Development

To modify the model or training, refer to `RFW_dataset_classification_using_LVM,CLIP(2).ipynb`

To customize the UI, edit `templates/index.html`

## Requirements

- Python 3.8+
- PyTorch 2.0+
- CLIP model
- 4GB+ RAM (8GB+ with GPU)
- GPU optional but recommended for faster predictions

## License

Educational project for Semester 7

## Author Notes

This web application provides an easy-to-use interface for your race classification model, making it accessible to anyone without coding knowledge. The model uses CLIP's powerful vision-language capabilities to achieve high accuracy in multi-class classification.
