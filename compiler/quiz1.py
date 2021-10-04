from tkinter import *
from tkinter import messagebox as mb

def game():
    root = Tk()
    root.geometry("800x500")
    root.title("Quiz")
    ques=[
     "1.What is the maximum possible length of an identifier in Python?",
     "2.Who developed Python language?",
     "3.Which one of the following is correct extension of Python file?",
     "4.What do we use to define a block of code in Python?",
     "5.What is the method inside the class in Python language?"
     ]
    options=[
     ["16", "32", "Not defined", "None of these"],
     ["Zim Den","Guido Van Rossum","Niene Stom","Wick Van Rossum"],
     [".py", ".python", ".p", "All of these"],
     ["key","Brackets","Identation","None of these"],
     ["Object", "Function", "Attribute", "Argument"]
     ]
    ans=[ 3, 2, 1, 3, 2]

    class Quiz:
        def __init__(self):
            self.qn = 0
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn):
            t = Label(root, text="Quiz", width=50, bg="red", fg="blue", font=("Monotype Corsiva", 20, "bold"))
            t.place(x=0, y=2)
            qn = Label(root, text=ques[qn], width=60, font=("Monotype Corsiva", 16, "bold"), anchor="w")
            qn.place(x=70, y=100)
            return qn

        def radiobtns(self):
            val = 0
            b = []
            yp = 150
            while val < 4:
                btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("Monotype Corsiva", 14))
                b.append(btn)
                btn.place(x=100, y=yp)
                val += 1
                yp += 40
            return b

        def display_options(self, qn):
            val = 0
            self.opt_selected.set(0)
            self.ques['text'] = ques[qn]
            for op in options[qn]:
                self.opts[val]['text'] = op
                val += 1

        def buttons(self):
            nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
            nbutton.place(x=200,y=380)
            quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
            quitbutton.place(x=380,y=380)

        def checkans(self, qn):
            if self.opt_selected.get() == ans[qn]:
                return True
            
        def nextbtn(self):
            if self.checkans(self.qn):
                self.correct += 1
            self.qn += 1
            if self.qn == len(ques):
                self.display_result()
            else:
                self.display_options(self.qn)       
            

        def display_result(self):
            score = int(self.correct / len(ques) * 100)
            result = "Score: " + str(score) + "%"
            wc = len(ques) - self.correct
            correct = "No. of correct answers: " + str(self.correct)
            wrong = "No. of wrong answers: " + str(wc)
            mb.showinfo("Result", "\n".join([result, correct, wrong]))



    quiz=Quiz()
    root.mainloop()
