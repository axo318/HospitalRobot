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

    def widgestsQuestions(self):

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
        self.YES.config(height = 5 , width = 15
        self.YES.grid(row=2,column=0)

        self.NO = Button(self)
        self.NO["bg"] = "red"
        self.NO["fg"] = "white"
        self.NO["font"] = "Ariel 30"
        self.NO["text"] = "NO"
        self.NO["command"] = self.patientNO
        self.NO.config(height = 5 , width = 15)
        self.NO.grid(row = 2, column = 1, padx = (10,0))

        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)

        self.sayQuestion(self.q)

    def patientYES(self):
        patientRs[patientQs[self.questionNum]] = "YES"
        self.questionNum += 1
        if self.questionNum >4:
            self.startFollow()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q
        self.sayQuestion(self.q)

    def patientNO(self):
        patientRs[patientQs[self.questionNum]] = "NO"
        self.questionNum += 1
        if self.questionNum >4:
            self.startFollow()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q
        self.sayQuestion(self.q)

    def sayQuestion(self,q):
        engine = pyttsx.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume',4)
        engine.say(q)
        engine.runAndWait()

    def clearGrid(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()

    def startQuestions(self):
        self.clearGrid()
        self.widgestsQuestions()

    def startHelp(self):
        self.clearGrid()
        self.widgetHelp()

    def widgetConsent(self):
        self.papaConsent = Label(self)
        self.papaConsent["text"] = "PapaDoc"
        self.papaConsent["font"] = "Ariel 30"
        self.papaConsent.grid(row=0, column=0 , columnspan = 2)


        self.lblConsent = Label(self)
        self.lblConsent["text"] = "Do You consent"
        self.lblConsent["font"] = "Ariel 30"
        self.lblConsent.grid(row=1,column=0, columnspan =2)

        self.btnYConsent = Button(self)
        self.btnYConsent["bg"] = "green"
        self.btnYConsent["fg"] = "white"
        self.btnYConsent["font"] = "Ariel 30"
        self.btnYConsent["text"] = "YES",
        self.btnYConsent["command"] = self.startQuestions
        self.btnYConsent.config(height = 5 , width = 15)
        self.btnYConsent.grid(row=2,column=0, padx = (10,0))

        self.btnNConsent = Button(self)
        self.btnNConsent["bg"] = "red"
        self.btnNConsent["fg"] = "white"
        self.btnNConsent["font"] = "Ariel 30"
        self.btnNConsent["text"] = "NO"
        self.btnNConsent["command"] = self.startFollow
        self.btnNConsent.config(height = 5 , width = 15)
        self.btnNConsent.grid(row = 2, column = 1,padx = (0,10))

        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)

        self.sayQuestion("Do You consent")



    def startFollow(self):
        self.clearGrid()
        self.widgetFollow()

    def widgetFollow(self):
        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN["font"] = "Ariel 30"
        self.MAIN.grid(row=0, column=0 , columnspan = 2)

        self.QUESTION = Label(self)
        self.QUESTION["text"] = "Follow Me"
        self.QUESTION["font"] = "Ariel 100"
        self.QUESTION.grid(row=1,column=0, columnspan =2)


        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)


    def widgetHelp(self):

        self.btnAlert = Button(self)
        self.btnAlert["bg"] = "orange"
        self.btnAlert["fg"] = "white"
        self.btnAlert["font"] = "Ariel 30"
        self.btnAlert["text"] = "Alert Staff"
        self.btnAlert["command"] = self.quit
        self.btnAlert.config(height = 5 , width = 30)
        self.btnAlert.grid(row = 1, column = 0)

    def widgetStart(self):
        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN["font"] = "Ariel 30"
        self.MAIN.grid(row=0, column=0 , columnspan = 2)

        self.QUESTION = Label(self)
        self.QUESTION["text"] = "Waiting for patient"
        self.QUESTION["font"] = "Ariel 100"
        self.QUESTION.grid(row=1,column=0, columnspan =2)


        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.questionNum = 0
        print(self.questionNum)
        master.title("PapaDoc")
        self.pack()
        self.widgetConsent()


patientQs = ["Do you smoke","Do you drink","Do you like Puppies", "Do you eat cheese", "Are you experiancing pain"]
patientRs = dict()

root = Tk()
root.attributes('-fullscreen',True)
app = Application(master=root)
app.mainloop()
root.destroy()

print(patientRs)
