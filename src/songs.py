import random
file1 = open('resources/happy.txt', 'r') 
H_songs=[]
while True:
        line=file1.readline();
        H_songs.append(line);
        if not line:
                break
file1.close()
file2 = open('resources/sad.txt', 'r') 
S_songs=[]
while True:
        line=file2.readline();
        S_songs.append(line);
        if not line:
                break
file2.close()
file3 = open('resources/fear.txt', 'r') 
F_songs=[]
while True:
        line=file3.readline();
        F_songs.append(line);
        if not line:
                break
file3.close()
file4 = open('resources/angry.txt', 'r') 
A_songs=[]
while True:
        line=file4.readline();
        A_songs.append(line);
        if not line:
                break
file4.close()
file5 = open('resources/neutral.txt', 'r') 
N_songs=[]
while True:
        line=file5.readline();
        N_songs.append(line);
        if not line:
                break
file5.close()
def predict_song(sentiment):
	if(sentiment==0):
		return random.choice(A_songs)
	elif(sentiment==1):
		return random.choice(F_songs)
	elif(sentiment==2):
		return random.choice(H_songs)
	elif(sentiment==3):
		return random.choice(N_songs)
	elif(sentiment==4):
		return random.choice(S_songs)