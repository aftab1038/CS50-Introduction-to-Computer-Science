from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")

        self.window.config(bg=THEME_COLOR)
        self.window.title("Quiz App")

        self.frame = Frame(self.window, bg=THEME_COLOR)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # self.score_label = Label(self.window, text="", bg=THEME_COLOR, fg="white")
        # self.score_label.pack()

        # Set a fixed canvas size
        canvas_width = 400
        canvas_height = 200
        self.canvas = Canvas(self.frame, width=canvas_width, height=canvas_height, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(canvas_width / 2, canvas_height / 2, width=350, text="hello", font=("Arial", 20, "italic"), anchor=CENTER)
        self.canvas.grid(row=0, column=0, pady=(50, 20), columnspan=2)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.false_button = Button(self.frame, image=self.false_image, command=self.check_answer_false)
        self.false_button.grid(row=1, column=0, padx=(20, 5))

        self.true_button = Button(self.frame, image=self.true_image, command=self.check_answer_true)
        self.true_button.grid(row=1, column=1, padx=(5, 20))

        self.get_next_question()

        self.window.mainloop()

    def show_score_popup(self):
        popup = Toplevel()
        popup.title("Quiz Score")
        score_label = Label(popup, text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
        score_label.pack()
        score_label.config(font=("Arial", 20, "italic"), anchor=CENTER)

        restart_button = Button(popup, text="Restart", command=self.restart_quiz)
        restart_button.pack()

        # close_button = Button(popup, text="Close", command=lambda: self.close_windows(popup))
        # close_button.pack()

        popup.mainloop()


    def restart_quiz(self):
        # Reset the quiz for a new round
        self.quiz.reset_quiz()

        # Get a new question
        self.get_next_question()

        # Close the popup
        self.close_windows(popup)
        popup.destroy()

    def close_windows(self, window):
        if self.window.winfo_exists():
            self.window.destroy()
        if window.winfo_exists():
            window.destroy()

    def get_next_question(self):
        self.canvas.config(bg="white")  # Reset canvas background color

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            
            # Adjust text font size to fit within the canvas
            text_length = len(question_text)
            font_size = 20
            while True:
                self.canvas.itemconfig(self.question_text, font=("Arial", font_size, "italic"))
                text_bbox = self.canvas.bbox(self.question_text)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                if text_width < 400 and text_height < 200:
                    break
                
                font_size -= 1
            
            # Set canvas size
            self.canvas.config(width=400, height=200)
        else:
            self.show_score_popup()

    def check_answer_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, user_answer):
        if user_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # self.score_label.config(text=f"")
        self.window.after(1000, self.get_next_question)
