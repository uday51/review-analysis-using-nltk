

import  nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag


nltk.download('averaged_perceptron_tagger_eng')
sia=SentimentIntensityAnalyzer()

review="The product quality is amazing! I received my order on time, and the packaging was great. However, the customer support was not very responsive."

review=review.lower()


#Sentence Tokenize
sentences=sent_tokenize(review)
print(sentences)

#Word Tokenize
words=[word_tokenize(sentence) for sentence in sentences ]
print(words)


#flatten words
words=[word for sublist in words for word in sublist]
print(words)

#Renoving Stop Words
stop_words=set(stopwords.words("english"))
filtered_words=[word for word in words if word not in stop_words]
print(filtered_words)

#pos
pos_tags=pos_tag(filtered_words)
print(pos_tags)

#Finding Noun
noun=[word for word,tag in pos_tags if tag in ["NN", "NNS", "NNP", "NNPS"]]
print(noun)










