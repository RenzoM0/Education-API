import json
from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import aiapi
from .models import Chat, LearningStyle, Rubric
from . import db

views = Blueprint('views', __name__)

@views.route('/' , methods=['POST', 'GET'])
@login_required
def home():
    aiapi.clear_chat_history()
    learningstyles = LearningStyle.query.filter_by(student=current_user.id).all()
    
    selected_learning_style_id = request.form.get('selected_learning_style')
    selected_learning_style = LearningStyle.query.get(selected_learning_style_id)
    if selected_learning_style:
        aiapi.add_personality(selected_learning_style.instruction)
    
    return render_template("home.html", user=current_user, learningstyles=learningstyles)

@views.route('/personality', methods=['POST', 'GET'])
@login_required
def personality():
    learningstyles = LearningStyle.query.filter_by(student=current_user.id).all()
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        instruction = request.form.get('instruction')
        
        new_learning_style = LearningStyle( name=name, description=description, instruction=instruction, student=current_user.id)
        db.session.add(new_learning_style)
        db.session.commit()
        flash("Learning style created", category='success')
        return redirect(url_for('views.personality'))

    return render_template("personality.html", user=current_user, learningstyles=learningstyles)

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
            res['answer'] = aiapi.generateChat(prompt, 2) 
            return jsonify(res), 200
        
    return render_template("c_interface_course2.html", user=current_user)

@login_required
@views.route('/grade', methods=['POST', 'GET'])
def grade():
    rubrics = Rubric.query.all()
    selected_rubric_id = request.form.get('selected_rubric')
    selected_rubric = Rubric.query.get(selected_rubric_id)
    rubric_instruction = None
    
    if selected_rubric:
        rubric_instruction = selected_rubric.rubric_instruction
    
    if request.method == 'POST':
        if 'commit' in request.form:  # Check if the 'commit' button was pressed
            chatdata = aiapi.get_chat_history()
            # Convert chatdata to a JSON string
            chatdata_json = json.dumps(chatdata)
        
            # Create a new Chat object and save it to the database
            new_chat = Chat(course='Grade Research', chatlog=chatdata_json, student=current_user.id)
            db.session.add(new_chat)
            db.session.commit()
            flash('Chat history saved!', category='success')
        else:    
            prompt = request.form['prompt']
            res = {}
            res['answer'] = aiapi.generateGrade(rubric_instruction, prompt)
            return jsonify(res), 200
    
    return render_template("grade.html", user=current_user, rubrics=rubrics, rubric_instruction=rubric_instruction)