from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from . import aiapi

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@login_required
@views.route("/course1chat", methods=['POST', 'GET'])
def course1chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChat(prompt, 1)
        return jsonify(res), 200
        
    return render_template("c_interface_course1.html", user=current_user)

@login_required
@views.route("/course2chat", methods=['POST', 'GET'])
def course2chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChat(prompt, 2)
        return jsonify(res), 200
        
    return render_template("c_interface_course2.html", user=current_user)