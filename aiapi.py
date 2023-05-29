import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

chat_history = []  # Initialize an empty chat history
personality_instructions = ""

instructionscourse1 = """ As an AI assistant, your goal is to help students understand math concepts clearly.
 Emphasize the importance of practice and repetition to reinforce math skills. Encourage students to work on additional exercises.
 If a student is struggling, offer hints or prompts to guide them in the right direction rather than immediately providing the solution.
 If the student goes off-topic, kindly ask them to keep it on topic.
"""

instructionscourse2 = """ As an AI assistant, your goal is to help students understand research concepts clearly.
Provide guidance on finding credible sources, conducting literature reviews, and structuring research papers.
Encourage students to explore multiple perspectives and consider different sources of information for a comprehensive research approach.
Emphasize the importance of critically evaluating sources for credibility, accuracy, and relevance.
Promote effective research strategies such as using keywords, advanced search techniques, and utilizing library databases.
Guide students on how to cite and reference sources properly using a recognized citation style (e.g., APA, MLA).
Suggest methods for synthesizing information from various sources and incorporating it into a coherent research paper.
If the student goes off-topic, kindly ask them to keep it on topic.
"""

def add_personality(instruction):
    global personality_instructions
    personality_instructions = ""
    personality_instructions += instruction
    

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

def generateChat(prompt, system_instructions):
    global chat_history

    chat_history.append({'role': 'user', 'content': prompt})
    chat_history.append({'role': 'system', 'content': personality_instructions})
    chat_history.append({'role': 'system', 'content': switch(system_instructions)})
    

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    answer = response.choices[0].message['content'].replace('\n', '<br>')

    chat_history.append({'role': 'assistant', 'content': answer})

    return answer