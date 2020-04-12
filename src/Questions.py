import random

def getQuestions():
    file1 = open('resources/mainQuestions.txt', 'r') 
    questions=[]
    while True:
            line=file1.readline();
            questions.append(line);
            if not line:
                    break
    file1.close()
    return questions

def chooseNextQuestion(questions, constraints = None):
    return random.choice(questions)
