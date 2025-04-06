from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Goal, Milestone, Certificate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///career_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    goals = Goal.query.all()
    certificates = Certificate.query.all()
    return render_template('index.html', goals=goals, certificates=certificates)

@app.route('/add_goal', methods=['POST'])
def add_goal():
    title = request.form.get('title')
    description = request.form.get('description')
    category = request.form.get('category')
    
    new_goal = Goal(title=title, description=description, category=category)
    db.session.add(new_goal)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/update_goal/<int:goal_id>', methods=['POST'])
def update_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    goal.progress = request.form.get('progress', type=int)
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/add_certificate', methods=['POST'])
def add_certificate():
    title = request.form.get('title')
    issuer = request.form.get('issuer')
    date_earned = request.form.get('date_earned')
    
    new_certificate = Certificate(title=title, issuer=issuer, date_earned=date_earned)
    db.session.add(new_certificate)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/get_career_suggestions', methods=['GET'])
def get_career_suggestions():
    # Simple career suggestion logic based on completed goals and certificates
    goals = Goal.query.filter_by(progress=100).all()
    certificates = Certificate.query.all()
    
    suggestions = []
    for goal in goals:
        if 'python' in goal.title.lower():
            suggestions.extend(['Python Developer', 'Data Scientist', 'Backend Developer'])
        elif 'aws' in goal.title.lower():
            suggestions.extend(['Cloud Engineer', 'DevOps Engineer', 'Solutions Architect'])
    
    return jsonify(list(set(suggestions)))

if __name__ == '__main__':
    app.run(debug=True)