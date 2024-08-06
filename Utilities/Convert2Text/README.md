# Create a README.md file with instructions for creating a virtual environment and running the script

content = """
# Speech to Text Application

This application converts speech from an audio file to text using the `speech_recognition` library.

## Setup

Follow these steps to set up the virtual environment and run the application:

1. **Create a Virtual Environment**

    ```bash
    python3 -m venv .venv
    ```

2. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        .venv\\Scripts\\activate
        ```

    - On macOS and Linux:

        ```bash
        source .venv/bin/activate
        ```

3. **Install the Required Packages**

    ```bash
    pip install SpeechRecognition
    ```
or 
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Script**

    Save the following script as `speech_to_text.py`:

    ```python
    import speech_recognition as sr

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Load the audio file
    audio_path = "path_to_your_audio_file.m4a"

    # Recognize the speech from the audio file
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='vi-VN')

    print(text)
    ```

    Replace `path_to_your_audio_file.m4a` with the path to your audio file.

    Run the script:

    ```bash
    python speech_to_text.py
    ```

## Deactivate the Virtual Environment

After you're done, deactivate the virtual environment:

```bash
deactivate
