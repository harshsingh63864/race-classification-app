# 🚀 Quick Start Guide - Race Classification Web App

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM (8GB+ with GPU recommended)
- Modern web browser (Chrome, Firefox, Edge, Safari)

## Installation & Setup

### Option 1: Windows (Easiest)

1. **Navigate to project folder**
   ```bash
   cd f:\Project-final
   ```

2. **Run the startup script**
   ```bash
   run.bat
   ```

   This will:
   - Check if Python is installed
   - Install dependencies from `requirements.txt`
   - Verify the model file exists
   - Start the Flask application

3. **Open in browser**
   - Navigate to: `http://localhost:5000`

---

### Option 2: Manual Setup (All Platforms)

#### Step 1: Install Dependencies

```bash
# Navigate to project directory
cd f:\Project-final

# Install required packages
pip install -r requirements.txt
```

If the above doesn't work, install individually:
```bash
pip install flask
pip install torch torchvision
pip install git+https://github.com/openai/CLIP.git
pip install pillow numpy scikit-learn werkzeug
```

#### Step 2: Verify Model File
Make sure `clip_lvm_model.pt` exists in `f:\Project-final\`

#### Step 3: Run the Application

**Option A - Python Script (Cross-platform)**
```bash
python run.py
```

**Option B - Python Direct**
```bash
python app.py
```

**Option C - Windows Batch**
```bash
run.bat
```

#### Step 4: Access the Application
Open your web browser and go to:
```
http://localhost:5000
```

---

## Using the Web Application

### 1. Upload Image
- Click **"📁 Choose File"** button
- Select a facial image (JPG, PNG, GIF, WebP)
- Image preview will appear

### 2. Make Prediction
- Click **"🚀 Predict"** button
- Wait for analysis (usually 2-5 seconds)

### 3. View Results
- See predicted race category
- View confidence percentage
- Compare scores for all 4 categories
- Analysis includes reasoning with confidence threshold

### 4. Next Prediction
- Click **"🔄 Clear"** to reset form
- Upload a new image and repeat

---

## Features Overview

### Overview Tab (Prediction)
- Upload images
- Get predictions
- See confidence scores
- View detailed results

### Features Tab
- Model information
- Technical details
- Classification categories
- Accuracy metrics

### About Tab
- Project description
- Technologies used
- Important ethical notice
- Responsible AI guidelines

---

## Troubleshooting

### Issue: "Port 5000 already in use"
**Solution:** 
```bash
# Edit app.py and change port number, e.g., to 5001:
python app.py --port 5001
```

### Issue: "clip_lvm_model.pt not found"
**Solution:** 
- Ensure the file exists in `f:\Project-final\`
- Check file name is exactly `clip_lvm_model.pt`
- Re-download if corrupted

### Issue: "ModuleNotFoundError: No module named 'clip'"
**Solution:**
```bash
pip install --upgrade git+https://github.com/openai/CLIP.git
```

### Issue: "CUDA out of memory"
**Solution:**
- The app will automatically fall back to CPU
- Or close other GPU-intensive applications
- Reduce image resolution if possible

### Issue: "No module named 'flask'"
**Solution:**
```bash
pip install -r requirements.txt
# or
pip install flask
```

---

## File Structure

```
f:\Project-final\
├── 📄 README.md                    # Full documentation
├── 📄 SETUP.md                     # This file
├── 🐍 app.py                       # Flask backend (main application)
├── 🐍 run.py                       # Python startup script
├── 💾 run.bat                      # Windows startup script
├── 📋 requirements.txt             # Python dependencies
├── 📕 clip_lvm_model.pt           # Pre-trained model
├── 📓 RFW_dataset_...ipynb        # Training notebook
│
├── 📁 templates/
│   └── 📄 index.html              # Web interface
│
├── 📁 uploads/                     # (Auto-created) Uploaded images
│
├── 📁 data/                        # Original dataset
│   ├── Dataset.csv
│   ├── African/
│   ├── Asian/
│   ├── Caucasian/
│   └── Indian/
```

---

## API Usage (For Developers)

### Send prediction request from Python/JavaScript:

```javascript
// JavaScript example
const formData = new FormData();
formData.append('file', imageFile);

fetch('http://localhost:5000/predict', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => {
    console.log('Predicted:', data.predicted_label);
    console.log('Confidence:', data.confidence);
});
```

### Response Format:
```json
{
  "success": true,
  "predicted_label": "African",
  "confidence": 98.07,
  "image": "data:image/png;base64,...",
  "filename": "photo.jpg",
  "all_scores": {
    "African": 0.9807,
    "Asian": 0.0089,
    "Caucasian": 0.0087,
    "Indian": 0.0017
  }
}
```

---

## Performance Tips

1. **Faster Predictions**: Use GPU (CUDA compatible NVIDIA card)
   - Install CUDA: https://developer.nvidia.com/cuda-downloads
   - Install cuDNN: https://developer.nvidia.com/cudnn

2. **Better Results**: Use high-quality facial images
   - Good lighting
   - Face clearly visible
   - JPG or PNG format

3. **Optimize Storage**: Clear `uploads/` folder periodically
   ```bash
   rmdir /s uploads    # Windows
   rm -rf uploads      # Mac/Linux
   ```

---

## Security Notes

⚠️ **Important Security Information:**

1. **Development Mode**: Currently running in debug mode
   - For production, edit `app.py`:
   ```python
   app.run(debug=False, ...)
   ```

2. **File Upload Limits**: 16MB maximum file size
   - Modify in `app.py`: `MAX_CONTENT_LENGTH = 16 * 1024 * 1024`

3. **Privacy**: Uploaded images are stored in `uploads/` folder
   - Delete regularly for privacy
   - Don't share this folder publicly

---

## Model Information

- **Architecture**: OpenAI CLIP (Vision Transformer ViT-B/32)
- **Training Dataset**: RFW (Racial Faces in the Wild)
- **Classes**: 4 (African, Asian, Caucasian, Indian)
- **Approach**: Zero-shot learning via text-image similarity
- **Accuracy**: ~90.58% on validation set

---

## Ethical & Responsible Use

⚠️ **IMPORTANT DISCLAIMER:**

This model is for **educational and research purposes only**.

- ✗ Do NOT use for discriminatory purposes
- ✗ Do NOT rely solely on this for critical decisions
- ✓ Consider cultural and genetic variations
- ✓ Be aware of potential biases
- ✓ Use responsibly and ethically

The model may have limitations and biases. Always validate predictions with human judgment.

---

## Support & Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **CLIP Paper**: https://arxiv.org/abs/2103.14030
- **PyTorch**: https://pytorch.org/
- **RFW Dataset**: https://www.nist.gov/itl/iad/image-group/racial-faces-wild-rfw-dataset

---

## Questions?

Refer to `README.md` for detailed documentation or the Jupyter notebook for training details.

**Happy classifying! 🚀**
