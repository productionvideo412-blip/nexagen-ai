from flask import Blueprint, request, jsonify
from services.ollama_service import get_chat_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_chat_response(user_input)
    return jsonify({'response': response})
