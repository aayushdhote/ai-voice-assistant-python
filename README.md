Voice Assistant Powered by Python

Overview


This is a simple voice-activated virtual assistant written in Python. It listens for voice commands through a microphone, processes them using speech recognition, and performs tasks such as playing music on YouTube, telling the current time, providing Wikipedia summaries, or stopping the program. The assistant uses text-to-speech to respond audibly to user commands.

Features





Play Music/Videos: Say "play [song name]" to play a video on YouTube.



Current Time: Say "time" to hear the current time in 12-hour format (e.g., "02:30 PM").



Wikipedia Summaries: Say "who is [person]" to get a one-sentence summary from Wikipedia.



Exit Program: Say "stop" to terminate the assistant.

Requirements





Python: Version 3.6 or higher.



Libraries:





speech_recognition: For speech-to-text conversion.



pyttsx3: For text-to-speech output.



pywhatkit: For playing YouTube videos.



wikipedia: For fetching Wikipedia summaries.



Hardware: A working microphone and speakers.



Internet: Required for speech recognition (Google API), YouTube, and Wikipedia access.

Installation





Install Python: Ensure Python 3.6+ is installed. Download from python.org.



Install Dependencies: Run the following command to install required libraries:

pip install speechrecognition pyttsx3 pywhatkit wikipedia



Additional Setup:





On Windows, pyttsx3 should work out of the box.



On Linux, install espeak for text-to-speech: sudo apt-get install espeak.



On macOS, pyttsx3 uses the built-in system voices.

Usage





Run the Script:





Save the code in a file (e.g., assistant.py).



Run it using: python assistant.py.



Interact with the Assistant:





The assistant will display "✅ Assistant started..." and "🎤 Listening..." in the console.



Speak a command clearly into the microphone.



Example commands:





"play happy birthday" → Plays a YouTube video of "Happy Birthday."



"time" → Says the current time (e.g., "The current time is 02:30 PM").



"who is Albert Einstein" → Reads a one-sentence Wikipedia summary about Albert Einstein.



"stop" → Exits the program with "Goodbye!"



Error Handling:





If the speech is unclear, the assistant says, "Sorry, I did not understand that."



If there's a service issue (e.g., no internet), it says, "Sorry, there's a problem with the service."

Code Structure





talk(text): Converts text to speech using pyttsx3.



listen(): Captures and recognizes voice input using speech_recognition and Google's API.



run_assistant(): Processes commands and triggers appropriate actions.



Main Loop: Continuously listens for commands until "stop" is said.

Limitations





Requires an internet connection for speech recognition, YouTube, and Wikipedia.



Only responds to specific commands ("play," "time," "who is," "stop").



Wikipedia summaries are limited to one sentence.



May fail if the microphone is misconfigured or unavailable.



Limited error handling for network or hardware issues.

Potential Improvements





Add more commands (e.g., weather, reminders, news).



Support offline speech recognition.



Allow customizable Wikipedia summary lengths.



Enhance command parsing with natural language processing.



Improve error handling for microphone or network issues.

Troubleshooting





Microphone Issues: Ensure your microphone is properly configured and not muted.



No Sound: Check speaker settings and ensure pyttsx3 is properly installed.



Recognition Errors: Speak clearly and ensure a stable internet connection.



Library Errors: Verify all dependencies are installed correctly.

License

This project is open-source and available under the MIT License.
