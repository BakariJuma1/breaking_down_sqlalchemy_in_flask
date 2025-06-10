# app.py
from flask import Flask, jsonify
from config import Config
from extensions import db
from models import User  # triggers model import and registration

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to the Modular Flask App!'

@app.route('/users')
def users():
    all_users = User.query.all()
    return jsonify([user.to_dict() for user in all_users])

@app.route('/add/<name>/<location>')
def add_user(name, location):
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return f"User {user.name} from {user.location} added."

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
