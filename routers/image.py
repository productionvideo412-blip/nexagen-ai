from flask import Blueprint, request, jsonify
from services.comfyui_service import generate_image

image_bp = Blueprint('image', __name__)

@image_bp.route('/image', methods=['POST'])
def image():
    prompt = request.json.get('prompt')
    image_url = generate_image(prompt)
    return jsonify({'image_url': image_url})
