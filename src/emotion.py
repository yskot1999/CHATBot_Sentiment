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

nltk.download('stopwords')

dirname = os.path.dirname(__file__)
filename_ngram= os.path.join(dirname, '../models/ngram.pkl')
ngram=joblib.load(filename_ngram)
filename_linear=os.path.join(dirname, '../models/linear.pkl')
linear=joblib.load(filename_linear)

def predict(user_response):
	#print(user_response)
	processedInp = preprocessResponse(user_response)
	fittedInp = ngram.transform(processedInp)
	#moods=linear.predict(fittedInp)
	print(processedInp)
	#print(moods)

""" preprocess the user input and returns in the form of an array"""
def preprocessResponse(user_response):
	corpus=[]
	review=re.sub('[^a-zA-Z]',' ',user_response)
	review=review.lower()
	review=review.split()
	ps=PorterStemmer()
	review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
	review=' '.join(review)
	corpus.append(review)
	return corpus
