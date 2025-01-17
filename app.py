from flask import Flask, request, jsonify, render_template
from src.MaliciousQRCodeDetection.pipeline.prediction import PredictionPipeline
import os

app = Flask(__name__)

# Initialize the PredictionPipeline
pipeline = PredictionPipeline()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        try:
            # Save the uploaded image temporarily
            file_path = os.path.join('temp', file.filename)
            os.makedirs('temp', exist_ok=True)
            file.save(file_path)
            
            # Process the QR code using PredictionPipeline
            qr_url = pipeline.get_url(file_path)
            predictions = pipeline.predict_url(qr_url)
            
            # Cleanup the temporary file
            os.remove(file_path)
            
            # Prepare the result
            result_html = f"""
                <div class='prediction-result'>
                    <p><strong>QR URL:</strong> {qr_url}</p>
                    <p><strong>Prediction:</strong> {'Safe' if predictions < 0.5 else 'Not Safe'}</p>
                </div>
            """
            return jsonify({'predictions_html': result_html})
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
