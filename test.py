import os
import cv2
import numpy as np
import pytesseract
import gradio as gr
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to extract text using TesserOCR
def extract_text(image):
    if isinstance(image, np.ndarray):  # If Gradio passes a NumPy array
        img = image
    else:  # If it's a file path
        img = cv2.imread(image)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

# Flask endpoint for OCR processing
@app.route('/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    extracted_text = extract_text(filepath)
    return jsonify({'extracted_text': extracted_text})

# Gradio interface
def gradio_ocr(img):
    if img is None:
        return "No image provided"
    
    extracted_text = extract_text(img)
    return extracted_text

iface = gr.Interface(fn=gradio_ocr, inputs="image", outputs="text")

if __name__ == '__main__':
    iface.launch(share=True)
    app.run(debug=True)
