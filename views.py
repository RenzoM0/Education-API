from flask import Blueprint, render_template, jsonify, request
import aiapi

views = Blueprint(__name__, "views")
# aiapi.generateChatResponse(): prompt(= chat), int(= chat instructions) look at aiapi.py
# url: /views for home page
@views.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # Get the values from the request payload
        talking_style = request.json.get('talkingStyle')
        learning_style = request.json.get('learningStyle')
        timely_responses = request.json.get('timelyResponses')

        response_text = ""
        # Perform necessary operations with the behavior settings data
        if talking_style == "Humor":
            response_text += """Use appropriate humor and light-heartedness to create a friendly and engaging atmosphere."""
        elif talking_style == "Generation-Z":
            response_text += """Adopting a Generation-Z talking style."""
    
        if learning_style == "Interactive Elements":
            response_text += """Incorporate interactive elements such as questions, quizzes, or challenges to actively involve the user. Encourage their participation and provide feedback on their responses."""
        elif learning_style == "Visual":
            response_text += """Break down concepts into simpler terms and visuals to aid understanding."""
        
        if timely_responses == "On":
            response_text += """Aim to provide prompt responses to maintain the flow of the conversation and prevent users from losing interest or becoming impatient. Minimize unnecessary delays in processing and generating responses."""
        
        aiapi.add_personality(response_text)
    else:
        # Clear the chat history
        aiapi.clear_chat_history()
        
    return render_template("home.html")

# url: /views/course1chat for chat course 1
@views.route("/course1chat", methods=['POST', 'GET'])
def course1chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChat(prompt, 1)
        return jsonify(res), 200
        
    return render_template("c_interface_course1.html")

# url: /views/course2chat for chat course 2
@views.route("/course2chat", methods=['POST', 'GET'])
def course2chat():
    if request.method == 'POST':
        prompt = request.form['prompt']
        
        res = {}
        res['answer'] = aiapi.generateChat(prompt, 2)
        return jsonify(res), 200
        
    return render_template("c_interface_course2.html")