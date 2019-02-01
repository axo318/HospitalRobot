#Title: AskQuestion  Author: TonyD  Created:2019-02-01
#Asks the user a question of either  open or, yes no
#Designed to be an open template that can be expanded on later with UI elements
#----CHANGES----
#2019-02-01 TonyD: Created File

import csv

#TonyD: Imports the questions from a csv file and then calls the ynQuesntion method
#TODO: Adapt to match database output
def loadQuestions():
    with open("QuestionsTest.csv",newline ='') as csvfile:
        questionReader = csv.reader(csvfile,delimiter=',',quotechar='|')
        for row in questionReader:
            for question in row:
                ynQuesntion(question)

#Tony: Used to ask the users questions currently just in terminal
#TODO: add UI and Return to
def ynQuesntion(q):
    #speakQuestion(q)
    answer = input(q)
    answer.upper()
    if answer == "YES" or answer == "NO" :
        print("ACCEPTED RESPONSE")
    else:
        print("INVALID RESPONSE")
        ynQuesntion(q)

#TonyD: This will use the voice engine to speak the questtion to the user
#TODO: Create 
#def speakQuestion(q):

#TonyD: This is the MAIN secion of the progam all calls through here
qtext = "does this work?"
loadQuestions()
ynQuesntion(qtext)
