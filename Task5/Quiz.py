import tkinter as tk
from tkinter import messagebox
import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Tamil Nadu", "Salem", "Goa"],
        "correct_answer": "Delhi",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": "Jupiter",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["3", "5", "6", "7"],
        "correct_answer": "7",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon dioxide",
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["African elephant", "Blue whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue whale",
    },
    {
        "question": 'Who wrote the play "Romeo and Juliet"?',
        "options": [
            "Charles Dickens",
            "Mark Twain",
            "William Shakespeare",
            "Jane Austen",
        ],
        "correct_answer": "William Shakespeare",
    },
    {
        "question": 'Which planet is known as the "Red Planet"?',
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the chemical symbol for the element gold?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "correct_answer": "Au",
    },
    {
        "question": "Which of the following is not a primary color?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "correct_answer": "Yellow",
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Brain", "Skin", "Lungs"],
        "correct_answer": "Skin",
    },
    {
        "question": "Which gas makes up the majority of the Earth's atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"],
        "correct_answer": "Nitrogen",
    },
]

current_question = 0
score = 0


def check_answer():
    global current_question, score

    user_answer = var.get()
    correct_answer = questions[current_question]["correct_answer"]

    if user_answer == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        next_button.config(state=tk.DISABLED)
        if score == 0:
            messagebox.showinfo(
                "Quiz Completed",
                f"Better Luck Next Time \nYour score is: {score} out of {len(questions)}",
            )
        else:
            messagebox.showinfo(
                "Quiz Completed",
                f"Congratulations! \nYour score is: {score} out of {len(questions)}",
            )
        message_box = messagebox.askyesno(
            "Play Again", "Do you want to Play Again?\nThis will Delete all your score \nAre you sure?"
        )
        if message_box == True:
            current_question = 0
            score = 0
            next_button.config(state=tk.NORMAL)
            root.mainloop()
        else:
            message_box = messagebox.askyesno(
                "Need Answers?", "Do you want to explore the answers?"
            )
            if message_box == True:
                for i in range(1, len(questions) + 1):
                    messagebox.showinfo(
                        i,
                        questions[i - 1]["question"]
                        + "\n"
                        + "\n"
                        + questions[i - 1]["correct_answer"],
                    )
                message_box = messagebox.askyesno(
                    "Play Again", "Do you want to Play Again?\nThis will Delete all your score \nAre you sure?"
                )
                if message_box == True:
                    current_question = 0
                    score = 0
                    next_button.config(state=tk.NORMAL)
                    root.mainloop()
                else:
                    messagebox.showinfo("Greetings", "Bye Bye\nSee You Later!")
            else:
                messagebox.showinfo("Greetings", "Bye Bye\nSee You Later!")


def show_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        radio_buttons[i - 1].config(text=option, value=option)


root = tk.Tk()
root.title("Quiz Game")
root.geometry("650x300+375+200")

question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

var = tk.StringVar()
radio_buttons = []

for i in range(4):
    radio_button = tk.Radiobutton(root, text="", variable=var)
    radio_button.pack()
    radio_buttons.append(radio_button)

next_button = tk.Button(root, text="Next", command=check_answer)
next_button.pack(pady=20)

messagebox.showinfo("Greetings", "Welcome to the Quiz Game!")
messagebox.showinfo(
    "Rules",
    "You will be asked multiple-choice questions. \nChoose the correct option to earn points.",
)
messagebox.showinfo("Start", "Let's get started!\n")

show_question()

root.mainloop()
