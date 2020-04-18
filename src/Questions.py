import random
file1 = open('resources/happy_questions.txt', 'r') 
H_questions=[]
while True:
        line=file1.readline();
        H_questions.append(line);
        if not line:
                break
file1.close()
file2 = open('resources/sad_questions.txt', 'r') 
S_questions=[]
while True:
        line=file2.readline();
        S_questions.append(line);
        if not line:
                break
file2.close()
file3 = open('resources/fear_questions.txt', 'r') 
F_questions=[]
while True:
        line=file3.readline();
        F_questions.append(line);
        if not line:
                break
file3.close()
file4 = open('resources/angry_questions.txt', 'r') 
A_questions=[]
while True:
        line=file4.readline();
        A_questions.append(line);
        if not line:
                break
file4.close()
file5 = open('resources/neutral_questions.txt', 'r') 
N_questions=[]
while True:
        line=file5.readline();
        N_questions.append(line);
        if not line:
                break
file5.close()

def chooseNextQuestion(emotion):
    if(emotion==0):
        return random.choice(A_questions)
    elif(emotion==1):
        return random.choice(F_questions)
    elif(emotion==2):
        return random.choice(H_questions)
    elif(emotion==3):
        return random.choice(N_questions)
    elif(emotion==4):
        return random.choice(S_questions)
