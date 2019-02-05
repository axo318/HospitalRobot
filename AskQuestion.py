#Title: AskQuestion  Author: TonyD  Created:2019-02-01
#Asks the user a question of either  open or, yes no
#Designed to be an open template that can be expanded on later with UI elements
#----CHANGES----
#2019-02-01 TonyD: Created File
#2019-02-05 TonyD: Added TTS and commentend all changes

import csv
import pyttsx


#TonyD: Imports the questions from a csv file and then calls the ynQuesntion method
#TODO: Adapt to match database output
def loadQuestions():
    answers = []
    engine = pyttsx.init()

    with open("QuestionsTest.csv") as csvfile:
        questionReader = csv.reader(csvfile,delimiter=',',quotechar='|')
        for row in questionReader:
            for question in row:
                answers.append(ynQuesntion(question,engine))
    return answers

#Tony: Used to ask the users questions currently just in terminal
#Tony: Now Contains the TTS calls a
#TODO: add UI code
def ynQuesntion(q,e):

    b = raw_input("Press any Key to Continue")
    e.say(q)
    e.runAndWait()
    answer = raw_input(q)

    if answer == "YES" or answer == "NO" :
        print("ACCEPTED RESPONSE")
        return answer
    else:
        print("INVALID RESPONSE")
        answer = ynQuesntion(q,e)
        return answer


#TonyD: This is the MAIN secion of the progam all calls through here

#This is The Start TTS
engine = pyttsx.init()
engine.say("Questions Now Begin")
engine.runAndWait()

answers = loadQuestions()

print("Responses were as follows")
print(answers)
