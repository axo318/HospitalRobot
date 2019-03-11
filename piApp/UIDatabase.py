#Title: AskQuestion  Author: TonyD  Created:2019-02-22
#Using Python 2 in order to add text to speach DONT CHANGE!!!!!
#The Main UI For Papa Doc
#----CHANGES----
#2019-02-22 TonyD: Created File
#2019-02-22 TonyD: Working UI
#----NEXT----


from Tkinter import *
import MySQLdb
import os
import pyttsx

class Application(Frame):

    def widgestsQuestions(self,patientQs):

        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN["font"] = "Ariel 30"
        self.MAIN.grid(row=0, column=0 , columnspan = 2)

        self.q = self.patientQs[self.questionNum]
        self.QUESTION = Label(self)
        self.QUESTION["text"] = self.q
        self.QUESTION["font"] = "Ariel 30"
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
        self.NO.config(height = 5, width = 15)
        self.NO.grid(row = 2, column = 1)

        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)

        #self.sayQuestion(self.q)

    def patientYES(self):
        patientRs[self.patientQs[self.questionNum]] = "YES"
        self.questionNum += 1
        if self.questionNum >4:
            self.startFollow()
        self.q = self.patientQs[self.questionNum]
        self.QUESTION["text"] = self.q
        #self.sayQuestion(self.q)

    def patientNO(self):
        patientRs[self.patientQs[self.questionNum]] = "NO"
        self.questionNum += 1
        if self.questionNum >4:
            self.startFollow()
        self.q = self.patientQs[self.questionNum]
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

    def startConsent(self):
        self.clearGrid()
        self.widgetConsent()

    def startQuestions(self):
        self.clearGrid()
        self.patientQs = self.getData()
        self.widgestsQuestions(self.patientQs)

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
        self.btnYConsent.grid(row=2,column=0)

        self.btnNConsent = Button(self)
        self.btnNConsent["bg"] = "red"
        self.btnNConsent["fg"] = "white"
        self.btnNConsent["font"] = "Ariel 30"
        self.btnNConsent["text"] = "NO"
        self.btnNConsent["command"] = self.startFollow
        self.btnNConsent.config(height = 5 , width = 15)
        self.btnNConsent.grid(row = 2, column = 1)

        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)

        #self.sayQuestion("Do You consent")


    def startFollow(self):
        self.clearGrid()
        self.pushData()
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
        self.btnHelp["command"] = self.finishedTrip
        self.btnHelp["text"] = "At destination"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)

        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)
    def finishedTrip(self):
        os.remove("piAppStart.txt")
        open("piAppStart.txt",'a').close
        self.startWait()

    def widgetHelp(self):

        self.btnAlert = Button(self)
        self.btnAlert["bg"] = "orange"
        self.btnAlert["fg"] = "white"
        self.btnAlert["font"] = "Ariel 30"
        self.btnAlert["text"] = "Alert Staff"
        self.btnAlert["command"] = self.quit
        self.btnAlert.config(height = 5 , width = 30)
        self.btnAlert.grid(row = 1, column = 0)

    def widgetosStart(self):
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

    def startWait(self):
        self.clearGrid()
        self.widgetWait()

    def widgetWait(self):

        self.btnWait = Button(self)
        self.btnWait["bg"] = "green"
        self.btnWait["fg"] = "white"
        self.btnWait["font"] = "Ariel 30"
        self.btnWait["command"] = self.check
        self.btnWait["text"] = "Ready To Start"
        self.btnWait.grid(row = 2, column = 0, columnspan = 2)

        self.btnHelp = Button(self)
        self.btnHelp["bg"] = "orange"
        self.btnHelp["fg"] = "white"
        self.btnHelp["font"] = "Ariel 30"
        self.btnHelp["command"] = self.startHelp
        self.btnHelp["text"] = "HELP"
        self.btnHelp.grid(row = 3, column = 0, columnspan = 2)


    def check(self):
        check = os.stat("piAppStart.txt").st_size == 0
        while(check):
            check = os.stat("piAppStart.txt").st_size == 0
        if(check == False):
            self.startConsent()

    def getData(self):

        db = MySQLdb.connect("localhost","root","password","sdp17" )
        cursor = db.cursor()
        department = "Cardiology"
        self.patient = "Tony"
        self.appdate = "2019-10-10"
        # execute SQL query using execute() method.
        cursor.execute("SELECT Question from Questions WHERE Department = '%s'" % (department))

        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        db.close
        return data



    def pushData(self):
        db = MySQLdb.connect("localhost","root","password","sdp17" )
        cursor = db.cursor()
        i = 0
        # execute SQL query using execute() method.
        for row in patientRs:
                r = patientRs[self.patientQs[i]]
                q = self.patientQs[i]
                i = i+1
                cursor.execute("INSERT INTO Responses (patient, appDate, question, response) VALUES (%s, %s, %s, %s)", (self.patient, self.appdate, q, r))
        db.commit()
        # Fetch a single row using fetchone() method.
        cursor.execute("UPDATE Appointments SET answered='Yes' WHERE (patient=%s and appDate=%s)", (self.patient, self.appdate))
        # disconnect from server
        db.commit()
        db.close

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.questionNum = 0
        print(self.questionNum)
        master.title("PapaDoc")
        self.pack()
        self.startWait()

patientRs = dict()

root = Tk()
root.attributes('-fullscreen',True)
app = Application(master=root)
app.mainloop()
root.destroy()
