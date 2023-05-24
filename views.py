from flask import Blueprint, render_template, jsonify, request
import aiapi

views = Blueprint(__name__, "views")
# aiapi.generateChatResponse(): prompt(= chat), int(= chat instructions) look at aiapi.py
# url: /views for home page
@views.route("/")
def home():
    return render_template("home.html")
# url: /views/chat for chat interface(test)
@views.route("/chat", methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt, 0)
        return jsonify(res), 200
        
    return render_template("c_interface.html")
# url: /views/course1chat for chat course 1
@views.route("/course1chat", methods=['POST', 'GET'])
def course1chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt, 1)
        return jsonify(res), 200
        
    return render_template("c_interface_course1.html")
# url: /views/course2chat for chat course 2
@views.route("/course2chat", methods=['POST', 'GET'])
def course2chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt, 2)
        return jsonify(res), 200
        
    return render_template("c_interface_course2.html")