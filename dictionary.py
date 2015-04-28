from sys import argv
from stemming.porter2 import stem
import nltk
from nltk.corpus import stopwords

def makeDict():
	f = open("subjclueslen1-HLTEMNLP05.tff", 'r')
	text = f.readlines()
	dictionary = {}

	for line in text:
		line = line.split()
		magnitude = line[0][5:] #['weaksubj', 'strongsubj']
	
		length = line[1][4:] #['1']
		word = line[2][6:]
		pos = line[3][5:]	#['noun', 'verb', 'adj', 'adverb', 'anypos']
		stem = line[4][9:]	#['y', '1', 'n']
		polarity = line[5][14:]	#['', 'ive', 'both', 'positive', 'negative', 'neutral']
		value = (magnitude, length, pos, stem, polarity)
		dictionary.update({word:value})


	return dictionary



