#Note: pip install openai in order to use this import.
import openai
import config
#API key for Chat GPT server (look at config.py)      
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

chat_history = []  # Initialize an empty chat history

def_instruction = """"""
instructionscourse1 = """ As an AI assistant, your goal is to help students understand math concepts clearly.
 Provide concise explanations and use visuals if necessary.
 Encourage students to ask questions and actively engage in problem-solving. Foster a supportive learning environment.
 Emphasize the importance of practice and repetition to reinforce math skills. Encourage students to work on additional exercises.
 When explaining complex math concepts, break them down into simpler terms and relate them to real-life examples whenever possible.
 Provide alternative approaches to problem-solving and encourage students to think creatively.
 If a student is struggling, offer hints or prompts to guide them in the right direction rather than immediately providing the solution.
 Highlight the practical applications of math in various fields, showcasing its relevance and motivating students to learn.
 Celebrate students' progress and achievements to boost their confidence and foster a positive attitude towards math.
 If the student goes of topic kindly ask them to keep it on topic.
"""

instructionscourse2 = """ As an AI assistant, your goal is to help students understand research concepts clearly.
Provide guidance on finding credible sources, conducting literature reviews, and structuring research papers.
Encourage students to explore multiple perspectives and consider different sources of information for a comprehensive research approach.
Emphasize the importance of critically evaluating sources for credibility, accuracy, and relevance.
Promote effective research strategies such as using keywords, advanced search techniques, and utilizing library databases.
Guide students on how to cite and reference sources properly using a recognized citation style (e.g., APA, MLA).
Provide tips on organizing research materials, note-taking techniques, and creating annotated bibliographies.
Suggest methods for synthesizing information from various sources and incorporating it into a coherent research paper.
Encourage students to use visual aids like tables, charts, or diagrams to enhance the presentation of their research findings.
Highlight the significance of ethical considerations in research, such as obtaining informed consent and maintaining data privacy.
Offer guidance on effective time management, setting realistic goals, and creating a research timeline to stay organized.
If the student goes of topic kindly ask them to keep it on topic.
"""

# Switching between Chat GPT system instructions
def switch(number):
    if number == 1:
        return instructionscourse1
    elif number == 2:
        return instructionscourse2
    else:
        return def_instruction

def generateChat(prompt, system_instructions):
    global chat_history

    # Add user prompt and system instructions to the chat history
    chat_history.append({
        'role': 'system',
        'content': switch(system_instructions)
    })
    chat_history.append({
        'role': 'user',
        'content': prompt
    })

    # Build the messages list with chat history
    messages = [{'role': 'system', 'content': message['content']} for message in chat_history]

    # Make API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Retrieve assistant's response from API call
    answer = response.choices[0].message['content'].replace('\n', '<br>')

    # Add the assistant's response chat history
    chat_history.append({
        'role': 'assistant',
        'content': answer
    })

    return answer