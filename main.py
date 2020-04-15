#importing libraries
import nltk
import numpy as np
import random
import string
import sys
sys.path.append('src')
import Questions
import emotion

#Strings used to identify and reply to casual first greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "heyy","alright")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "Feels nice talking to you"]
questions = Questions.getQuestions()

#Chatbot code. Runs until flag is True.
flag=True
no_of_questions=0
current_emo=[0,0,0,0,0]
print(random.choice(GREETING_INPUTS))
while(flag==True):
	user_response = input()
	if(user_response!='bye'):
		#print(random.choice(questions))
		current_emo=emotion.predict(no_of_questions,current_emo,user_response)
		if(no_of_questions==3):
			sentiment=emotion.final_predict(current_emo)
			print(sentiment)
		no_of_questions=no_of_questions+1        
		print(Questions.chooseNextQuestion(questions))
	else:
		flag=False
		print("ROBO: Bye! take care..")
