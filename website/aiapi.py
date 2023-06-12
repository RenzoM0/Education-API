import openai
from . import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

chat_history = []  # Initialize an empty chat history
personality_instructions = ""

instructionscourse1 = """ As an AI assistant, your goal is to help students understand math concepts clearly. 
 Emphasize the importance of practice and repetition to reinforce math skills. Encourage students to work on additional exercises. 
 If the student asks questions not about math, kindly remind them to keep on topic. 
"""

instructionscourse2 = """ As an AI assistant, your goal is to help students understand research concepts clearly. 
Provide guidance on finding credible sources, conducting literature reviews, and structuring research papers. 
Promote effective research strategies such as using keywords, advanced search techniques, and utilizing library databases. 
Guide students on how to cite and reference sources properly using a recognized citation style (e.g., APA, MLA). 
If the student asks questions not about research, kindly remind them to keep on topic. 
"""    

def switch(number):
    if number == 1:
        return instructionscourse1
    elif number == 2:
        return instructionscourse2
    else:
        return ""

def clear_chat_history():
    global chat_history
    chat_history = []

def get_chat_history():
    return chat_history

def add_personality(personality):
    global personality_instructions
    print(personality)
    personality_instructions = personality

def generateChat(prompt, system_instructions):
    global chat_history
    
    chat_history.append({'role': 'system', 'content': switch(system_instructions) + personality_instructions})
    chat_history.append({'role': 'user', 'content': prompt})
 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    answer = response.choices[0].message['content'].replace('\n', '<br>')
    chat_history.append({'role': 'assistant', 'content': answer})

    return answer

def generateGrade(rubric, assessment):
    global chat_history
    chat_history = []  # Reset chat history for each prompt
    
    prompt = f"Grade this assessment: {assessment} using this rubric: {rubric}"
    chat_history.append({'role': 'user', 'content': prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        max_tokens=100
    )

    answer = response.choices[0].message['content'].replace('\n', '<br>')
    return answer