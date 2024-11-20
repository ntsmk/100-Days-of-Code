from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                           text="Dream is the most important. Even more important than actual life. Dream won’t die.",
                           font=("Arial", 20, "italic"), width=260)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="White")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(2000, self.get_next_question)


