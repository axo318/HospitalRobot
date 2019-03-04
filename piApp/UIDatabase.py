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

class Application(Frame):

    def createWidgets(self):

        self.MAIN = Label(self)
        self.MAIN["text"] = "PapaDoc"
        self.MAIN["font"] = ("Helvetica", 40)
        self.MAIN.pack()

        self.q = patientQs[self.questionNum]
        self.QUESTION = Label(self)
        self.QUESTION["text"] = self.q
        self.QUESTION["font"] = ("Helvetica", 26)
        self.QUESTION.pack()

        self.YES = Button(self)
        self.YES["bg"] = "green"
        self.YES["height"] = "10"
        self.YES["width"] = "15"
        self.YES["fg"] = "white"
        self.YES["text"] = "YES"
        self.YES["font"] = ("Helvetica", 24)
        self.YES["command"] = self.patientYES
        self.YES.pack({"side": "left"})

        self.NO = Button(self)
        self.NO["bg"] = "red"
        self.NO["height"] = "10"
        self.NO["width"] = "15"
        self.NO["fg"] = "white"
        self.NO["text"] = "NO"
        self.NO["font"] = ("Helvetica", 24)
        self.NO["command"] = self.patientNO
        self.NO.pack({"side":"left"})


    def patientYES(self):
        patientRs[patientQs[self.questionNum]] = "Yes"
        self.questionNum += 1
        if self.questionNum >(len(data)-1):
            self.quit()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q

    def patientNO(self):
        patientRs[patientQs[self.questionNum]] = "No"
        self.questionNum += 1
        if self.questionNum >(len(data)-1):
            self.quit()
        self.q = patientQs[self.questionNum]
        self.QUESTION["text"] = self.q


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.questionNum = 0
        master.title("PapaDoc")
        self.pack()
        self.createWidgets()

db = MySQLdb.connect("localhost","root","password","sdp17" )
cursor = db.cursor()
department = sys.argv[1]
patient = sys.argv[2]
appdate = sys.argv[3]
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

self.quit();
