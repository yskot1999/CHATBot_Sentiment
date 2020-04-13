def predict(user_response):
	print(user_response)
	import re
	import nltk
	nltk.download('stopwords')
	from nltk.corpus import stopwords
	from nltk.stem.porter import PorterStemmer
	corpus=[]
	review=re.sub('[^a-zA-Z]',' ',user_response)
	review=review.lower()
	review=review.split()
	ps=PorterStemmer()
	review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
	review=' '.join(review)
	corpus.append(review)
	print(corpus)
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn.preprocessing import LabelEncoder,OneHotEncoder
	from sklearn.svm import LinearSVC
	from sklearn.metrics import accuracy_score
	from sklearn.model_selection import train_test_split
	from sklearn.externals import joblib
	import sys
	sys.path.append('../models')
	ngram=joblib.load('ngram.pkl')
