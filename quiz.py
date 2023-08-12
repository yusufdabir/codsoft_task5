import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.configure(bg="lightgray")
        
        self.score = 0
        self.current_question = 0
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Madrid", "Rome", "Berlin"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "Which famous scientist developed the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "correct_answer": "Albert Einstein"
            }
        ]
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16), bg="lightgray")
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", font=("Helvetica", 12), variable=self.var, value="", bg="lightgray", command=self.check_answer)
            self.radio_buttons.append(rb)
            rb.pack(anchor=tk.W)
        
        self.next_button = tk.Button(root, text="Next", font=("Helvetica", 12), state=tk.DISABLED, command=self.next_question)
        self.next_button.pack(pady=20)
        
        self.load_question(self.current_question)

    def load_question(self, question_idx):
        self.var.set("")
        self.question_label.config(text=self.questions[question_idx]["question"])
        options = self.questions[question_idx]["options"]
        random.shuffle(options)
        for i in range(4):
            self.radio_buttons[i].config(text=options[i], value=options[i])
        self.next_button.config(state=tk.DISABLED)
    
    def check_answer(self):
        user_answer = self.var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showerror("Incorrect", f"Incorrect answer! Correct answer is {correct_answer}")
        self.next_button.config(state=tk.NORMAL)
        for rb in self.radio_buttons:
            rb.config(state=tk.DISABLED)
    
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question(self.current_question)
            for rb in self.radio_buttons:
                rb.config(state=tk.NORMAL)
        else:
            self.show_final_results()
    
    def show_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.score = 0
            self.current_question = 0
            self.load_question(self.current_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
