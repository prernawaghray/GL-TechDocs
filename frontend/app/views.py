from flask import render_template
from app import app

@app.route('/')
def home():
   return render_template('home-page/home.html')

@app.route('/dashboard')
def dashboard():
   return render_template('user-dashboard/dashboard.html')
