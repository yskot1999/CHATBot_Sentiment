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
filename_ngram= os.path.join(dirname, '../models/ngram.pkl')
ngram=joblib.load(filename_ngram)
filename_linear=os.path.join(dirname, '../models/linearSVC.pkl')
linear=joblib.load(filename_linear)
filename_random=os.path.join(dirname, '../models/random.pkl')
random_model=joblib.load(filename_random)

def predict(no_of_questions,current_emo,user_response):
	#print(user_response)
	processedInp = preprocessResponse(user_response)
	fittedInp = ngram.transform(processedInp)
	moods1=linear.predict_proba(fittedInp)
	current_emo=calcAverage(no_of_questions,current_emo,moods1)
	moods2=random_model.predict_proba(fittedInp)
	print(processedInp)

        # Order of emotions: Anger, Happy , Hate, Sad, Worry
	print("Linear SVC:")
	print(moods1)
	print("Random forest:")
	print(moods2)
	return current_emo

""" predicts the final mood """
def final_predict(current_emo):
	print(current_emo)
	if((0.60>=current_emo[3]>=0.50) and current_emo[4]>=0.10):
		return 4
	elif((0.50>=current_emo[1]>=0.20) and current_emo[3]>0.60):
		return 5
	else:
		maxindex=0
		maxvalue=0
		for i in range(len(current_emo)):
			if(current_emo[i]>=maxvalue):
				maxindex=i
				maxvalue=current_emo[i]
		return maxindex
""" calculates the average of a function """
def calcAverage(no_of_questions,current_emo,moods1):
	for i in range(len(moods1[0])):
		moods1[0][i]=((current_emo[i]*no_of_questions) + moods1[0][i])/(no_of_questions + 1)
	return moods1[0]
""" preprocess the user input and returns in the form of an array"""
def preprocessResponse(user_response):
	corpus=[]
	review=str(user_response).encode('ascii','ignore').decode('ascii')
	review=re.sub('[^a-zA-Z]',' ',review)
	review=review.lower()
	review=review.split()
	ps=PorterStemmer()
	review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
	review=' '.join(review)
	corpus.append(review)
	return corpus
