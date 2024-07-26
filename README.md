# Genie-A-Voice-Assistant
Genie is a versatile and intelligent voice assistant designed to streamline your daily tasks and enhance productivity.

## Description

The Virtual Assistant is a desktop application designed to assist users with various tasks using voice commands. It features functionalities like web searches, opening applications, playing media, managing to-do lists, reading PDF files, setting reminders, and more. The assistant is built using Python and leverages libraries such as SpeechRecognition, pywhatkit, pyjokes, and others.

## Features

- **Voice Commands**: Activate the assistant and control various functions through voice commands.
- **Web Searches**: Perform Google searches and Wikipedia lookups.
- **Application Management**: Open and close applications like Chrome and Brave.
- **Media Playback**: Play videos and music.
- **PDF Reading**: Read PDF files aloud.
- **Reminders and To-Do Lists**: Manage reminders and maintain a to-do list.
- **Notes**: Write, show, and append notes.
- **Weather and News**: Get current weather updates and latest news.
- **Crypto Information**: Retrieve cryptocurrency prices.
- **System Commands**: Perform system operations like shutdown, restart, and lock.

## Installation

To use the Virtual Assistant, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/virtual-assistant.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd virtual-assistant
    ```

3. **Install Dependencies**:

    Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Assistant**:

    ```bash
    python assistant.py
    ```

2. **Interact with the Assistant**:
   - Use the wake word to activate the assistant.
   - Issue commands such as "play music", "open Chrome", "set reminder", etc.

## Commands

Here are some example commands you can use:

- **"google search [query]"**: Performs a Google search for the specified query.
- **"open chat gpt"**: Opens ChatGPT in Chrome.
- **"play music [title]"**: Plays the specified song.
- **"read pdf [file name]"**: Reads the specified PDF file aloud.
- **"set alarm"**: Sets an alarm based on your input.
- **"tell me a joke"**: Provides a random joke.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top-right of the repository page.

2. **Clone Your Fork**:

    ```bash
    git clone https://github.com/yourusername/virtual-assistant.git
    ```

3. **Create a New Branch**:

    ```bash
    git checkout -b feature-branch
    ```

4. **Make Changes and Commit**:

    ```bash
    git add .
    git commit -m "Add feature"
    ```

5. **Push to Your Fork**:

    ```bash
    git push origin feature-branch
    ```

6. **Create a Pull Request**: Go to the original repository and create a pull request from your fork.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **SpeechRecognition**: For handling speech-to-text conversion.
- **pywhatkit**: For performing web searches and other tasks.
- **pyjokes**: For generating random jokes.
- **[Your Collaborators]**: For contributing to the development of this project.
