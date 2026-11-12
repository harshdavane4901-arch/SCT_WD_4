# Student Study Assistant

## Project Overview

The Student Study Assistant is a simple conversational assistant developed using Python. It simulates a multi-turn conversation and provides students with basic study guidance, learning suggestions, and practice prompts.

The project demonstrates how an assistant can respond to different user messages using predefined rules and maintain basic context during a conversation.

## Objectives

- Build a simple conversational assistant.
- Simulate multiple dialogue turns.
- Create a defined assistant persona.
- Maintain basic conversation context.
- Generate consistent responses.
- Save conversation history in JSON format.

## Technologies Used

- Python 3
- JSON
- Visual Studio Code / Notepad
- GitHub

## Features

1. Personalized greetings.
2. User name recognition.
3. Subject selection.
4. Basic learning explanations.
5. Study tips and suggestions.
6. Quiz practice prompts.
7. Help command.
8. Conversation history saving.
9. Basic error handling.

## How the Assistant Works

The assistant follows these steps:

1. Starts the program and displays a welcome message.
2. Receives a message from the user.
3. Checks the message using predefined conditions.
4. Identifies the user's intended command.
5. Generates a suitable response.
6. Maintains the user's name and selected subject during the session.
7. Stores conversation exchanges.
8. Saves the conversation in a JSON file when the user exits.

## Project Structure

```text
StudentStudyAssistant/
│
├── assistant.py
├── README.md
└── sample_conversation.txt
```

The `conversation_log.json` file is generated automatically when the program runs and is not included in the public repository.

## Installation and Setup

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

### Step 2: Download the Project

Clone or download this repository to your computer.

### Step 3: Run the Program

Open Command Prompt inside the project folder and execute:

```bash
python assistant.py
```

### Step 4: Start the Conversation

Type your messages and interact with the assistant.

Use `help` to see the available commands and `exit` to finish.

## Sample Commands

| User Command | Function |
|---|---|
| Hi | Starts a greeting |
| My name is Neha | Saves the user's name |
| Study Python | Selects a subject |
| Explain | Provides learning guidance |
| Study tips | Provides study suggestions |
| Quiz | Starts a practice prompt |
| Help | Displays available commands |
| Exit | Ends the conversation |

## Improvements Made

- Created a defined assistant persona.
- Added multiple response conditions.
- Added basic context management.
- Added a default response for unsupported messages.
- Added input validation for empty messages.
- Added JSON conversation logging.
- Added error handling for saving conversation files.

## Limitations

This project is a rule-based simulation. It does not use a live AI model or understand every possible question. Its responses depend on predefined conditions and its context is limited to the current session.

## Future Improvements

- Add a graphical user interface.
- Integrate an AI language model.
- Add more subjects and learning topics.
- Improve intent recognition.
- Add quizzes with actual questions and answer checking.

## Conclusion

This project demonstrates the basic working of a simulated conversational assistant using Python. It helped me understand conversation flow, conditional logic, object-oriented programming, user input handling, and JSON file management.

**Internship Project: Task 04 – Simulating an Assistant**
