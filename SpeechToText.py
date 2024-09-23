import speech_recognition as sr
import serial  # For communicating with Arduino

# Initialize speech recognition
recognizer = sr.Recognizer()

# List of bad words to trigger the relay
bad_words = ['horny', 'fuck', 'shit', 'bitch', 'ass', 'asshole', 'cunt', 'dick', 'breeding', 'dicks','pp', 'peepee', 'erect', 'breeding', 'Vaporeon', 'acid', 'wet', 'sore', 'nipples', 'water', 'Pokemon',]

# Set up serial communication with Arduino
arduino = serial.Serial('COM12', 9600)  # Replace 'COM12' with the correct port for your Arduino

# Function to trigger the relay via Arduino
def trigger_relay():
    arduino.write(b'1')  # Send the signal to Arduino to trigger the relay
    print("Relay Triggered!")

# Function to detect bad words
def detect_bad_words(text):
    for word in bad_words:
        if word in text.lower():
            return True
    return False

# Callback function to process the audio in real-time
def callback(recognizer, audio):
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")

        # Check for bad words
        if detect_bad_words(text):
            trigger_relay()

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    # Set up the microphone
    mic = sr.Microphone()

    # Adjust for ambient noise
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    print("Listening in real-time...")

    # Start a background listener with the callback function
    stop_listening = recognizer.listen_in_background(mic, callback)

    try:
        while True:
            # Keep the main thread running while the background thread listens
            pass
    except KeyboardInterrupt:
        print("Stopping...")
        stop_listening()
