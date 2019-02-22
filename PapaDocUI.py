#Title: AskQuestion  Author: TonyD  Created:2019-02-22
#Using Python 2 in order to add text to speach DONT CHANGE!!!!!
#The Main UI For Papa Doc
#----CHANGES----
#2019-02-22 TonyD: Created File
#2019-02-22 TonyD: Working UI
#----NEXT----
#Integrate with database
#Improve User Experiance 
#Integrate with TTS may have issues here


from Tkinter import *

class Application(Frame):

    def createWidgets(self):

        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN.pack()

        self.q = patientQs[self.questionNum]
        self.QUESTION = Label(self)
        self.QUESTION["text"] = self.q
        self.QUESTION.pack()

        self.YES = Button(self)
        self.YES["bg"] = "green"
        self.YES["fg"] = "white"
        self.YES["text"] = "YES",
        self.YES["command"] = self.patientYES
        self.YES.pack({"side": "left"})

        self.NO = Button(self)
        self.NO["bg"] = "red"
        self.NO["fg"] = "white"
        self.NO["text"] = "NO"
        self.NO["command"] = self.patientNO
        self.NO.pack({"side":"left"})


    def patientYES(self):
        patientRs[patientQs[self.questionNum]] = "YES"
        self.questionNum += 1
        if self.questionNum >4:
            self.quit()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q

    def patientNO(self):
        patientRs[patientQs[self.questionNum]] = "NO"
        self.questionNum += 1
        if self.questionNum >4:
            self.quit()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q


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
