import speech_recognition as sr
import openai
import os

# Import ElevenLabs
from elevenlabs import generate, play, set_api_key

# Set OpenAI API Key
openai.api_key = "Set OpenAI API Key"

# Set your ElevenLabs API key here
set_api_key("Set your ElevenLabs API key")

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
            # Use the speech recognition library to convert audio to text
            recognized_text = r.recognize_google(audio)
            print("You said:", recognized_text)
            return recognized_text.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
            return None
        except sr.RequestError as e:
            print(f"Error occurred during speech recognition: {e}")
            return None

# Function to generate response using OpenAI API
def generate_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.9
    )
    generated_text = response.choices[0].text.strip()
    print("OpenAI Response:", generated_text)
    return generated_text

# Rest of the code...

# Start the conversation with a greeting
speak_text("Hello Sir! What are we working on today?")

# Loop infinitely for user to speak
while True:
    try:
        recognized_text = listen_to_speech()
        if recognized_text is not None:
            openai_response = generate_openai_response(recognized_text)
            # Perform actions based on OpenAI response
            # You can add logic to handle specific actions based on the response
            if "create" in openai_response:
                # Handle create action
                pass
            elif "read" in openai_response:
                # Handle read action
                pass
            elif "modify" in openai_response:
                # Handle modify action
                pass
            else:
                # Handle other actions or responses
                pass

            # Speak the OpenAI response
            speak_text(openai_response)
        else:
            speak_text("I'm having trouble with the audio. Could you please repeat, sir?")

    except KeyboardInterrupt:
        print("Program stopped by the user.")
        break
