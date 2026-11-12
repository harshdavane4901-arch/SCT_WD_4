
"""
Project: Student Study Assistant
Internship Task: Simulating an Assistant

This program demonstrates:
1. A defined assistant persona
2. A sequence of prompts
3. Multi-turn conversations
4. Basic context memory
5. Consistent responses
"""

import json
from datetime import datetime


class StudentStudyAssistant:
    """A simple study assistant that maintains session context."""

    def __init__(self):
        self.name = ""
        self.subject = "General Studies"
        self.conversation = []

        self.greetings = [
            "Hello",
            "Hi",
            "Hey",
            "Good morning",
            "Good afternoon",
        ]

    def respond(self, message):
        """Generate a response based on the user's message."""

        message = message.strip()
        lower_message = message.lower()

        if not message:
            return "Please type a message so I can help you."

        # Step 1: Identify the user's name.
        if lower_message.startswith("my name is "):
            self.name = message[11:].strip().split()[0].capitalize()
            return f"Nice to meet you, {self.name}! What subject would you like to study?"

        # Step 2: Remember the selected subject.
        if (
            lower_message.startswith("study ")
            and not lower_message.startswith("study tip")
        ):
            new_subject = message[6:].strip().rstrip("?.!")

            if not new_subject:
                return "Please enter a subject, for example: study Python."

            self.subject = new_subject.title()

            return (
                f"Great! I will help you with {self.subject}. "
                "You can ask for an explanation, a study tip, or a quiz."
            )

        # Step 3: Handle greetings.
        if any(lower_message.startswith(g.lower()) for g in self.greetings):
            if self.name:
                return f"Hello, {self.name}! What would you like to learn today?"
            return "Hello! I am your Student Study Assistant. What is your name?"

        # Step 4: Explain the current subject.
        if "explain" in lower_message or "teach me" in lower_message:
            return (
                f"Let's learn about {self.subject}. "
                "First, understand the basic definition. "
                "Next, study one example. Finally, explain the concept "
                "in your own words to check your understanding."
            )

        # Step 5: Give study advice.
        if "study tip" in lower_message or "study tips" in lower_message:
            return (
                f"Here is a study tip for {self.subject}: "
                "Study for 25 minutes, take a 5-minute break, "
                "and then answer three practice questions."
            )

        # Step 6: Start a simple quiz.
        if "quiz" in lower_message or "test me" in lower_message:
            return (
                f"Let's practise {self.subject}! "
                "Tell me one important concept you have learned, "
                "and I will help you review it."
            )

        # Step 7: Handle requests for help.
        if "help" in lower_message or "options" in lower_message:
            return (
                "Here is what I can do:\n"
                "1. Type 'study Python' to choose a subject.\n"
                "2. Type 'explain' to get a learning plan.\n"
                "3. Type 'study tips' for study advice.\n"
                "4. Type 'quiz' to practise.\n"
                "5. Type 'exit' to end the conversation."
            )

        # Step 8: Default response.
        return (
            f"I am here to help you study {self.subject}. "
            "Try asking me to explain a topic, give study tips, "
            "or start a quiz. Type 'help' to see all options."
        )

    def run(self):
        """Run the assistant and save the conversation."""

        print("=" * 50)
        print("       STUDENT STUDY ASSISTANT")
        print("=" * 50)
        print("Your personal study helper is ready!")
        print("Type 'help' to see available commands.")
        print("Type 'exit' to finish.\n")

        while True:
            user_message = input("You: ").strip()

            if user_message.lower() in ("exit", "quit", "bye"):
                farewell = (
                    f"Goodbye, {self.name}! Keep learning!"
                    if self.name
                    else "Goodbye! Keep learning!"
                )
                print("Assistant:", farewell)
                self.conversation.append({
                    "user": user_message,
                    "assistant": farewell,
                })
                break

            assistant_reply = self.respond(user_message)

            print("Assistant:", assistant_reply, "\n")

            self.conversation.append({
                "user": user_message,
                "assistant": assistant_reply,
            })

        self.save_conversation()

    def save_conversation(self):
        """Save the session as a JSON conversation log."""

        filename = "conversation_log.json"

        log_data = {
            "project": "Student Study Assistant",
            "date": datetime.now().isoformat(timespec="seconds"),
            "student_name": self.name or "Not provided",
            "subject": self.subject,
            "conversation": self.conversation,
        }

        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(log_data, file, indent=4, ensure_ascii=False)

            print(f"Conversation saved to {filename}")

        except OSError as error:
            print(f"Could not save conversation: {error}")


if __name__ == "__main__":
    assistant = StudentStudyAssistant()
    assistant.run()
