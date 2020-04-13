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
print(random.choice(GREETING_INPUTS));
while(flag==True):
	user_response = input()
	if(user_response!='bye'):
		#print(random.choice(questions))
		emotion.predict(user_response)        
		print(Questions.chooseNextQuestion(questions))
	else:
		flag=False
		print("ROBO: Bye! take care..")
