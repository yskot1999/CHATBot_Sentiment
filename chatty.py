#importing libraries
import nltk
import numpy as np
import random
import string

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "heyy","alright")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "Feels nice talking to you"]


"""def greeting(sentence):
    for word in sentence.split():
        if word in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)"""
file1 = open('questions.txt', 'r') 
questions=[]
while True:
	line=file1.readline();
	questions.append(line);
	if not line:
		break
file1.close()
flag=True
meeting_flag = True
print(random.choice(GREETING_INPUTS));
while(flag==True):
    user_response = input()
    #user_response=user_response.lower()
    if(user_response!='bye'):
    	print(random.choice(questions))        
    else:
        flag=False
        print("ROBO: Bye! take care..")