# Voice to Text

## Overview
This repository contains a **simple Python-based voice-to-text script** that captures audio from a microphone and converts spoken input into text using speech recognition libraries.

The project was built as a **learning-stage implementation** to understand how speech recognition works in practice. It is intentionally kept **script-based** and is **not designed as a backend service or production system**.


## What This Project Does
- Listens to audio input from the microphone
- Converts speech to text using Google Speech Recognition
- Prints the recognized text to the console
- Allows graceful termination by saying `exit`

The focus of this project is on:
- Handling microphone input
- Using speech recognition APIs
- Basic error handling and control flow



## How It Works (High Level)
1. The microphone captures audio input
2. Ambient noise is adjusted for better recognition
3. Audio is sent to the speech recognition engine
4. Transcribed text is returned and displayed
5. The program exits cleanly when the user says `exit`



## Tech Stack
- Python
- SpeechRecognition
- PyAudio


## Project Structure
```

Voice_to_Text/
│
├── voice_to_text.py
├── requirements.txt
└── README.md

````

## Setup & Run

### Prerequisites
- Python 3.x
- Microphone access
- System-level audio dependencies (required for PyAudio)

### Installation
```bash
pip install -r requirements.txt
````

### Run the script

```bash
python voice_to_text.py
```

Speak into the microphone.
Say **`exit`** to terminate the program.


## What This Project Is NOT

This repository does **not** include:

* Backend APIs
* Web services
* Async job processing
* System or service architecture
* Production-level reliability or scaling

For backend- and system-oriented projects, please refer to my **pinned repositories**.


## Why This Repository Is Public

This project is kept public to:

* Demonstrate early hands-on work with speech recognition
* Show learning progression toward backend + AI systems
* Maintain transparency in my development journey

It is **not part of my curated backend portfolio**.


## Possible Improvements (If Revisited)

* Modularize audio and recognition logic
* Improve error feedback
* Add configuration options
* Extend to file-based audio input
