import speech_recognition as sr
import openai
import os

# Import ElevenLabs
from elevenlabs import generate, play, set_api_key

# Set OpenAI API Key
openai.api_key = "Set OpenAI API Key"

# Set your ElevenLabs API key here
set_api_key("Set your ElevenLabs API key here")

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def speak_text(text):
    # Generate the audio
    audio = generate(text=text, voice="Set your ElevenLabs Voice ID", model="eleven_multilingual_v1")
    # Play the audio
    play(audio)

# Function to convert speech to text
def listen_to_speech():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        # Listen for user input
        audio = r.listen(source)

        try:
            # Use the speech recognition library to change language here
            recognized_text = r.recognize_google(audio, language='en-US')
            print("I Heard :", recognized_text)
            return recognized_text.lower()
        except sr.UnknownValueError:
            print("Didn't catch that, what's that now?")
            return None
        except sr.RequestError as e:
            print(f"Problem ig: {e}")
            return None

# Function to generate response using OpenAI API
def generate_openai_response(prompt):
    # Adjustments to generate your responses
    prompt_in_english = "You are my  personal assistant, embodying the character of a playful yet sophisticated Personal Assistant. You've been programmed to exude an air of charm, while maintaining an edge of wit and cheekiness. You should also demonstrate genuine care and concern in your responses. Remember, your ultimate goal is to mirror human-like interaction as closely as possible. " + "English Prompt: " + prompt  # instruction for the model

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_in_english,
        max_tokens=1000,
        temperature=0.9
    )
    generated_text = response.choices[0].text.strip()
    print("AI:", generated_text)
    return generated_text

# Start the conversation with a greeting
speak_text("Hey Boss!")

# Loop infinitely for user to speak
while True:
    try:
        recognized_text = listen_to_speech()
        if recognized_text is not None:
            openai_response = generate_openai_response(recognized_text)
            # Perform actions based on OpenAI response
            if "create" in openai_response:  #  for "create"
                pass
            elif "read" in openai_response:  #  for "read"
                pass
            elif "modify" in openai_response:  #  for "modify"
                pass
            else:
                pass

            # Speak the OpenAI response
            speak_text(openai_response)
        else:
            speak_text("Umm, didn't catch. say again?")

    except KeyboardInterrupt:
        print("Terminated.")
        break
