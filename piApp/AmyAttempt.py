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
import MySQLdb
import os

class Application(Frame):

    def startUP(self):
        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN["font"] = "Ariel 30"
        self.MAIN.grid(row=0, column=0 , columnspan = 2)

        self.START = Button(self)
        self.START["bg"] = "blue"
        self.START["fg"] = "white"
        self.START["font"] = "Ariel 30"
        self.START["text"] = "Click here to start",
        self.START["command"] = self.check
        self.START.config(height = 5 , width = 5)
        self.START.grid(row=2,column=0)
    def check(self):
        check = os.stat("piAppStart.txt").st_size == 0
        while(check):
            check = os.stat("piAppStart.txt").st_size == 0
        if(check == False):
            self.createWidgets()

    def createWidgets(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()

        self.q = patientQs[self.questionNum]
        self.QUESTION = Label(self)
        self.QUESTION["text"] = self.q
        self.QUESTION["font"] = "Ariel 40"
        self.QUESTION.grid(row=1,column=0, columnspan =4)

        self.YES = Button(self)
        self.YES["bg"] = "green"
        self.YES["fg"] = "white"
        self.YES["font"] = "Ariel 30"
        self.YES["text"] = "YES",
        self.YES["command"] = self.patientYES
        self.YES.config(height = 5 , width = 5)
        self.YES.grid(row=2,column=0)

        self.NO = Button(self)
        self.NO["bg"] = "red"
        self.NO["fg"] = "white"
        self.NO["font"] = "Ariel 30"
        self.NO["text"] = "NO"
        self.NO["command"] = self.patientNO
        self.NO.config(height = 5 , width = 5)
        self.NO.grid(row = 2, column = 1)


    def patientYES(self):
        patientRs[patientQs[self.questionNum]] = "Yes"
        self.questionNum += 1
        if self.questionNum >(len(data)-1):
            self.finishedQuestions()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q

    def patientNO(self):
        patientRs[patientQs[self.questionNum]] = "No"
        self.questionNum += 1
        if self.questionNum >(len(data)-1):
            self.finishedQuestions()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q

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
        master.title("PapaDoc")
        self.pack()
        self.startUP()

db = MySQLdb.connect("localhost","root","password","sdp17" )
cursor = db.cursor()
department = "Cardiology"
patient = "TestTxt"
appdate = "2019-10-10"
# execute SQL query using execute() method.
cursor.execute("SELECT Question from Questions WHERE Department = '%s'" % (department))

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print data

# disconnect from server
db.close

patientQs = data
patientRs = dict()

root = Tk()
root.attributes('-fullscreen',True)
app = Application(master=root)
app.mainloop()
root.destroy()

db = MySQLdb.connect("localhost","root","password","sdp17" )
cursor = db.cursor()
i = 0
# execute SQL query using execute() method.
for row in patientRs:
        r = patientRs[data[i]]
        q = data[i]
        i = i+1
        cursor.execute("INSERT INTO Responses (patient, appDate, question, response) VALUES (%s, %s, %s, %s)", (patient, appdate, q, r))
db.commit()
# Fetch a single row using fetchone() method.
cursor.execute("UPDATE Appointments SET answered='Yes' WHERE (patient=%s and appDate=%s)", (patient, appdate))
# disconnect from server
db.commit()
db.close
