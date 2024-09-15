import os
import sys
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './services/')))
from services.extract_text import extract_text

# Create a Blueprint for routing
upload_routes = Blueprint('upload_routes',__name__)


# Set allowed file extensions and upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),'../../data/')
ALLOWED_EXTENSIONS = {'pdf','docx','txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@upload_routes.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error':'No file part'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Extract text from file
        extracted_text = extract_text(file_path)
        print(extracted_text)
        return jsonify({'message': f'File {filename} uploaded successfully.', 'text': extracted_text}), 200
    
    return jsonify({'error':'File type not allowed'}), 400

