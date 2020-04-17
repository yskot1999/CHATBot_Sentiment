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
GREETING_INPUTS = ("Hello", "Hi", "Greetings", "Sup", "What's up", "Hey", "Heyy")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "Feels nice talking to you"]

#Strings to fill between 2 questions
SAD_FILLERS = ["That's bad", "I feel sorry for you", "I understand"]
HAPPY_FILLERS = ["Great", "Nice", "Woah"]

questions = Questions.getQuestions()


# Declare variables used.
flag=True
no_of_questions = 0
current_emo=[0,0,0,0,0]
current_mood = None

# Initialize conversation with a random starter.
print(random.choice(GREETING_INPUTS))

# Chatbot code. Runs until flag is True.
while(flag==True):
	user_response = input()
	if(user_response!='bye'):
		#print(random.choice(questions))
		current_emo=emotion.predict(no_of_questions,current_emo,user_response)
		if(no_of_questions == 3):
			sentiment=emotion.final_predict(current_emo)
			print(sentiment)
			break

		no_of_questions=no_of_questions+1        
		current_mood = emotion.final_predict(current_emo)
		print(current_mood)
		print(Questions.chooseNextQuestion(questions))

	else:
		flag=False
		print("ROBO: Bye! take care..")
