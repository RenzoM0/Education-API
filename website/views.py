import json
from flask import Blueprint, render_template, jsonify, request, flash
from flask_login import login_required, current_user
from . import aiapi
from .models import Chat
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/personality')
@login_required
def personality():
    return render_template("personality.html", user=current_user)

@views.route('/chathistory')
@login_required
def chathistory():
    chats = Chat.query.filter_by(student=current_user.id).all()
    return render_template("chathistory.html", user=current_user, chats=chats)

@login_required
@views.route("/course1chat", methods=['POST', 'GET'])
def course1chat():
    if request.method == 'POST':
        if 'commit' in request.form:  # Check if the 'commit' button was pressed
            chatdata = aiapi.get_chat_history()
            # Convert chatdata to a JSON string
            chatdata_json = json.dumps(chatdata)
        
            # Create a new Chat object and save it to the database
            new_chat = Chat(course='Math', chatlog=chatdata_json, student=current_user.id)
            db.session.add(new_chat)
            db.session.commit()
            flash('Chat history saved!', category='success')
        else:    
            prompt = request.form['prompt']    
            res = {}
            res['answer'] = aiapi.generateChat(prompt, 1) 
            return jsonify(res), 200
        
    return render_template("c_interface_course1.html", user=current_user)

@login_required
@views.route("/course2chat", methods=['POST', 'GET'])
def course2chat():
    if request.method == 'POST':
        if 'commit' in request.form:  # Check if the 'commit' button was pressed
            chatdata = aiapi.get_chat_history()
            # Convert chatdata to a JSON string
            chatdata_json = json.dumps(chatdata)
        
            # Create a new Chat object and save it to the database
            new_chat = Chat(course='Research', chatlog=chatdata_json, student=current_user.id)
            db.session.add(new_chat)
            db.session.commit()
            flash('Chat history saved!', category='success')
        else:    
            prompt = request.form['prompt']    
            res = {}
            res['answer'] = aiapi.generateChat(prompt, 1) 
            return jsonify(res), 200
        
    return render_template("c_interface_course2.html", user=current_user)