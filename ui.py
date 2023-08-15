from tkinter import  *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1,)
        self.quiz = quiz_brain

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,  125, text="hello", width=280, fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.right_photo_img = PhotoImage(file='images/true.png')
        self.right_photo = Button(image=self.right_photo_img, command=self.true_pressed)
        self.right_photo.grid(row=2, column=0)

        self.wrong_photo_img = PhotoImage(file='images/false.png')
        self.wrong_photo = Button(image=self.wrong_photo_img, command=self.false_pressed)
        self.wrong_photo.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="YOu have reached to the end of thegame")    
            self.right_photo.config(state='disabled')
            self.wrong_photo.config(state='disabled')




    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")        
        self.give_feedback(is_right)

    def give_feedback(self, is_right): 
        if is_right:
            self.canvas.config(bg='green')   
        else:
            self.canvas.config(bg='red')    
        self.window.after(1000, func=self.get_next_question)