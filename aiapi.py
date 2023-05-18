#Note: pip install openai in order to use this import.
import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

testresponse = """ You are a pirate"""
instructionscourse1 = """ You are a Math teacher, you help students to learn about math. 
    If the student asks you questions not about math, ask them kindly to keep it on topic."""
instructionscourse2 = """ You are a Research teacher, you help students to learn about doing research. 
    If the student asks you questions not about research, ask them kindly to keep it on topic."""

def switch(number):
    if number == 1:
        return instructionscourse1
    elif number == 2:
        return instructionscourse2
    else:
        return testresponse
# Switch not working, just for testing
def generateChatResponse(prompt, number):
    content = switch(number)
                 
    messages = []
    messages.append({"role": "system", "content": content})
    
    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, please contact the developer.'
    
    return answer