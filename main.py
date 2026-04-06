from flask import Flask
from routers.chat import chat_bp
from routers.image import image_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(chat_bp)
app.register_blueprint(image_bp)

if __name__ == '__main__':
    app.run(debug=True)
