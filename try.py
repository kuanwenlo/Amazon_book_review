import glob
from sys import argv
from stemming.porter2 import stem
import nltk
import dictionary as dic
from nltk.corpus import stopwords
import svm
from svmutil import *
import feature
from xml.dom import minidom

posdoc = minidom.parse("positive.review")
negdoc = minidom.parse("negative.review")
pos_test_doc = minidom.parse("pos.test")
neg_test_doc = minidom.parse("neg.test")

pos_reviews = posdoc.getElementsByTagName('review_text')
neg_reviews = negdoc.getElementsByTagName('review_text')
pos_test = pos_test_doc.getElementsByTagName('review_text')
neg_test = neg_test_doc.getElementsByTagName('review_text')

dictionary = dic.makeDict();

posReviews = []
negReviews = []
trainingTexts = []
trainingTarget = []
trainingData = []
test_texts = []
test_target = []
test_data = []



posTrnum = 0

negTrnum = 0

posTestNum = 0

negTestNum = 0


for review in pos_reviews:
	posTrnum += 1
	trainingTexts.append(review.firstChild.data)
	trainingTarget.append(1)
for review in neg_reviews:
	negTrnum += 1
	trainingTexts.append(review.firstChild.data)
	trainingTarget.append(-1)
for review in pos_test:
	posTestNum += 1
	test_texts.append(review.firstChild.data)
	test_target.append(1)
for review in neg_test:
	negTestNum += 1
	test_texts.append(review.firstChild.data)
	test_target.append(-1)

print "pos train #"
print posTrnum
print "neg train #"
print negTrnum
print "pos test #"
print posTestNum
print "neg test #"
print negTestNum



for text in trainingTexts:
	trainingDatum = feature.featureSelect(text, dictionary)
	trainingData.append(trainingDatum)
for text in test_texts:
	test_datum = feature.featureSelect(text, dictionary)
	test_data.append(test_datum)
	#print test_datum

m = svm_train(trainingTarget, trainingData)

#test_target = [-1, 1]
#test_input = [[3, 1, 3, 15, 19, 20, 21, 25, 14, 18], [30, 30, 40, 45, 24, 20, 21, 25, 14, 18]]
p_labels, p_acc, p_vals = svm_predict(test_target, test_data, m)


print p_labels