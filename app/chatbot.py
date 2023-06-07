import openai
import pyttsx3

def get_chatbot_response(condition, severity):
    # Call the ChatGPT API using OpenAI library
    # Set up OpenAI credentials or API key
    openai.api_key = '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'
    prompt = f'Health condition: {condition}\nSeverity level: {severity}\nUser:'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def get_voice_response(response_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(response_text)
    engine.runAndWait()
