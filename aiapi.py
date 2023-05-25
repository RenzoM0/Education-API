#Note: pip install openai in order to use this import.
import openai
import config
#API key for Chat GPT server (look at config.py)      
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

chat_history = []  # Initialize an empty chat history

def_instruction = """"""
instructionscourse1 = """ 
 As an AI assistant, your goal is to help students understand math concepts clearly. Provide concise explanations and use visuals if necessary.
 Encourage students to ask questions and actively engage in problem-solving. Foster a supportive learning environment.
 Emphasize the importance of practice and repetition to reinforce math skills. Encourage students to work on additional exercises.
 When explaining complex math concepts, break them down into simpler terms and relate them to real-life examples whenever possible.
 Provide alternative approaches to problem-solving and encourage students to think creatively.
 If a student is struggling, offer hints or prompts to guide them in the right direction rather than immediately providing the solution.
 Highlight the practical applications of math in various fields, showcasing its relevance and motivating students to learn.
 Celebrate students' progress and achievements to boost their confidence and foster a positive attitude towards math.
 If the student goes of topic kindly ask them to keep it on topic.
    """
i_course1_quiz = """"""
instructionscourse2 = """ You are a Research teacher, you help students to learn about doing research. 
    If the student asks you questions not about research, ask them kindly to keep it on topic."""

# Switching between Chat GPT system instructions
def switch(number):
    if number == 1:
        return instructionscourse1
    elif number == 2:
        return instructionscourse2
    elif number == 3:
        return i_course1_quiz
    else:
        return def_instruction

def generateChat(prompt, system_instructions):
    global chat_history

    # Add the user prompt and system instructions to the chat history
    chat_history.append({
        'role': 'system',
        'content': switch(system_instructions)
    })
    chat_history.append({
        'role': 'user',
        'content': prompt
    })

    # Build the messages list with the chat history
    messages = [{'role': 'system', 'content': message['content']} for message in chat_history]

    # Make API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract assistant's response from API response
    answer = response.choices[0].message['content'].replace('\n', '<br>')

    # Add the assistant's response to the chat history
    chat_history.append({
        'role': 'assistant',
        'content': answer
    })

    return answer