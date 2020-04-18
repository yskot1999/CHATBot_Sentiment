import re
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
"""
if (happy>20 and happy<50) and sad>50
	bored

"""
nltk.download('stopwords')

dirname = os.path.dirname(__file__)

filename_ngram_lat= os.path.join(dirname, '../models/ngramlat.pkl')
ngram_lat=joblib.load(filename_ngram_lat)

filename_linear_lat=os.path.join(dirname, '../models/svmlatproba.pkl')
linear_lat=joblib.load(filename_linear_lat)

filename_random=os.path.join(dirname, '../models/random.pkl')
random_model=joblib.load(filename_random)

filename_ngram=os.path.join(dirname, '../models/ngram.pkl')
ngram=joblib.load(filename_ngram)

filename_linear=os.path.join(dirname, '../models/linearSVC.pkl')
linear=joblib.load(filename_linear)

def predict(no_of_questions,current_emo,user_response):
	#print(user_response)
	processedInp , invert = preprocessResponse(user_response)
	fittedInp = ngram_lat.transform(processedInp)
	moods1=linear_lat.predict_proba(fittedInp)

        # If not encountered in current sentence. Do some modifications
        # to the returned probabilities.
	if(invert == True):
		print("Inverting...")
		maxint = 0
		maxval = 0
		for i in range(len(moods1[0])):
			if(moods1[0][i] >= maxval):
				maxval = moods1[0][i]
				maxint = i
                
                # If predicted mood is angry, change it to neutral with
                # 50% probability.
		if(maxint == 0):
			temp = moods1[0][0]
			moods1[0][0] = moods1[0][3]
			moods1[0][3] = 0.5

                # If predicted mood is fear, change it to neutral with
                # 50% probability.
		elif(maxint == 1):
			temp=moods1[0][1]
			moods1[0][1] = moods1[0][3]
			moods1[0][3] = 0.5

                # If predicted mood is happy, swap probabilities with 
                # sad.
		elif(maxint == 2):
			temp=moods1[0][2]
			moods1[0][2] = moods1[0][4]
			moods1[0][4] = temp

                # If predicted mood is sad, swap probabilities with 
                # happy. 
		elif(maxint == 4):
			temp=moods1[0][4]
			moods1[0][4] = moods1[0][2]
			moods1[0][2] = temp

	print("Current Prediction: ")
	print(moods1)
	current_emo = calcAverage(no_of_questions, current_emo,moods1)
	#moods2=random_model.predict_proba(fittedInp)
	print(processedInp)
    #Update Order of emotions: Anger, Fear , Happy, Neutral, Sad 
	"""
	print("Random forest:")
	print(moods2)
	print("Linear SVC:")
	print(moods3)
        """
	return current_emo

""" predicts the final mood """
def final_predict(current_emo):
	print("in fp")
	print(current_emo)

	maxindex=0
	secondIndex = 0
	maxvalue=0
	secondValue = 0

	for i in range(len(current_emo)):
		if(current_emo[i]>=maxvalue):
			secondIndex = maxindex
			maxindex=i
			secondValue = current_emo[secondIndex]
			maxvalue = current_emo[maxindex] 
			continue
		elif(maxvalue > current_emo[i] >= secondValue):
			secondIndex = i
			secondValue = current_emo[secondIndex]
			
	print(maxvalue)
	print(secondValue)
	return maxindex

""" calculates the average of a function """
def calcAverage(no_of_questions, current_emo, moods1):
	for i in range(len(moods1[0])):
	    moods1[0][i] = ((current_emo[i]*no_of_questions) + moods1[0][i])/(no_of_questions + 1)
	return moods1[0]

""" preprocess the user input and returns in the form of an array"""
def preprocessResponse(user_response):
	corpus=[]
	invert=True
	if "not" not in user_response:
		invert=False
	review=str(user_response).encode('ascii','ignore').decode('ascii')
	review=re.sub('[^a-zA-Z]',' ',review)
	review=review.lower()
	review=review.split()
	ps=PorterStemmer()
	review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
	review=' '.join(review)
	corpus.append(review)
	return corpus,invert
