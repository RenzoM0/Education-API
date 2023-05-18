from flask import Blueprint, render_template, jsonify, request
import aiapi

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/chat", methods=['POST', 'GET'])
def home2():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200
        
    return render_template("c_interface.html")