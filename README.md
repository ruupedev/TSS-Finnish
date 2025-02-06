# Minimal Text-to-Speech App

A simple Python application that converts text to speech using `gTTS` (Google Text-to-Speech) and plays the generated audio. The app is built with `tkinter` for the GUI.

## Features
- Accepts text input from the user
- Converts text to Finnish speech using `gTTS`
- Saves the audio as an MP3 file
- Plays the generated MP3 using the default system player

## Requirements
Make sure you have Python installed (version 3.x recommended). Install the required dependencies with:

```sh
pip install gtts
```

# Usage
Run the script using:
```sh
python TTS.py
```
## How It Works
1. Enter text in the input field.
2. Click the Render & Play button.
3. The text is converted to speech and played.

## Notes

- The audio file is saved temporarily and played via the system's default audio player.
- The application is designed to work with the Finnish (fi) language.

## License

This project is open-source and available under the MIT License.
