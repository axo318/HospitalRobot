#Title: AskQuestion  Author: TonyD  Created:2019-02-22
#Using Python 2 in order to add text to speach DONT CHANGE!!!!!
#The Main UI For Papa Doc
#----CHANGES----
#2019-02-22 TonyD: Created File
#2019-02-22 TonyD: Working UI
#----NEXT----
#Integrate with database


from Tkinter import *
import pyttsx

class Application(Frame):

    def createWidgets(self):

        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN["font"] = "Ariel 30"
        self.MAIN.grid(row=0, column=0 , columnspan = 2)

        self.q = patientQs[self.questionNum]
        self.QUESTION = Label(self)
        self.QUESTION["text"] = self.q
        self.QUESTION["font"] = "Ariel 40"
        self.QUESTION.grid(row=1,column=0, columnspan =2)

        self.YES = Button(self)
        self.YES["bg"] = "green"
        self.YES["fg"] = "white"
        self.YES["font"] = "Ariel 30"
        self.YES["text"] = "YES",
        self.YES["command"] = self.patientYES
        self.YES.config(height = 5 , width = 15)
        self.YES.grid(row=2,column=0)

        self.NO = Button(self)
        self.NO["bg"] = "red"
        self.NO["fg"] = "white"
        self.NO["font"] = "Ariel 30"
        self.NO["text"] = "NO"
        self.NO["command"] = self.patientNO
        self.NO.config(height = 5 , width = 15)
        self.NO.grid(row = 2, column = 1)

        self.sayQuestion(self.q)

    def patientYES(self):
        patientRs[patientQs[self.questionNum]] = "YES"
        self.questionNum += 1
        if self.questionNum >4:
            self.finishedQuestions()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q
        self.sayQuestion(self.q)

    def patientNO(self):
        patientRs[patientQs[self.questionNum]] = "NO"
        self.questionNum += 1
        if self.questionNum >4:
            self.finishedQuestions()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q
        self.sayQuestion(self.q)

    def sayQuestion(self,q):
        engine = pyttsx.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume',3)
        engine.say(q)
        engine.runAndWait()

    def finishedQuestions(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()

        self.QUIT = Button(self)
        self.QUIT["bg"] = "green"
        self.QUIT["fg"] = "white"
        self.QUIT["font"] = "Ariel 30"
        self.QUIT["text"] = "QUIT",
        self.QUIT["command"] = self.quit
        self.QUIT.config(height = 5 , width = 15)
        self.QUIT.grid(row=1,column=0)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.questionNum = 0
        print(self.questionNum)
        master.title("PapaDoc")
        self.pack()
        self.createWidgets()


patientQs = ["Do you smoke","Do you drink","Do you like Puppies", "Do you eat cheese", "Are you experiancing pain"]
patientRs = dict()

root = Tk()
root.attributes('-fullscreen',True)
app = Application(master=root)
app.mainloop()
root.destroy()

print(patientRs)
