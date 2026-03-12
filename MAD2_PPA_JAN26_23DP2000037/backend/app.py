from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_caching import Cache
from flask_cors import CORS
from config import Config
from models import db, User
from werkzeug.security import generate_password_hash

jwt = JWTManager()
mail = Mail()
cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    from routes import bp
    app.register_blueprint(bp, url_prefix='/api')

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(role='admin').first():
            db.session.add(User(username='admin', email='admin@placement.com',
                password=generate_password_hash('admin123'), role='admin'))
            db.session.commit()
    return app

# create a global WSGI application object so imports in serverless wrappers
# (or the vercel `api/app.py` helper) can grab it without re‑initializing.  
# Vercel's Python runtime looks for either ``app`` or ``handler`` in the
# entrypoint file.
app = create_app()

if __name__ == '__main__':
    # Local development
    app.run(debug=True, port=5000)
