stop = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']
negTag = ["isn't", "aren't", "hasn't", "haven't", "don't", "doesn't","ain't", "aint", "won't", "couldn't", "cannot", "can't", "not", "no", "neither", "nor", "shouldn't", "wouldn't"]

def featureSelect(text, dictionary):
	filtered_lines = [l for l in text.split('.')]
	posNoun = 0
	posVerb = 0
	posAdj = 0
	posAdv = 0
	posAny = 0
	negNoun = 0
	negVerb = 0
	negAdj = 0
	negAdv = 0
	negAny = 0 
	neuNoun = 0
	neuVerb = 0
	neuAdj = 0
	neuAdv = 0
	neuAny = 0 
	wordCount = 0
	for line in filtered_lines:
		#filtered_words = [w for w in line.split() if not w in stop]
		filtered_words = [w for w in line.split() ]
		neg = False
		for w in filtered_words:
			if w in negTag:
				neg = True
			if(dictionary.get(w) == None):
				continue
			else:
				#print w 
				fact = dictionary.get(w)
				if fact[0] == "weaksubj" :
					amp = 0.2 #0.13
				elif fact[0] == "strongsubj" :
					amp = 0.55 #0.55
				if (fact[4] == "positive" and neg == False) or ((fact[4] =='negative') and neg):
					
					if fact[2] == "noun" :
						posNoun += amp
					elif fact[2] == "verb" :
						posVerb += amp
					elif fact[2] == "adj" :
						posAdj += amp
					elif fact[2] == "adverb" :
						posAdv += amp
					elif fact[2] == "anypos":
						posAny += amp
				elif (fact[4] == "negative" and neg == False) or ((fact[4]=='positive') and neg ):
					
					if fact[2] == "noun" :
						negNoun += amp
					elif fact[2] == "verb" :
						negVerb += amp
					elif fact[2] == "adj" :
						negAdj += amp
					elif fact[2] == "adverb" :
						negAdv += amp
					elif fact[2] == "anypos":
						negAny += amp
				elif (fact[4] == "neutral"):
					if fact[2] == "noun" :
						neuNoun += amp
					elif fact[2] == "verb" :
						neuVerb += amp
					elif fact[2] == "adj" :
						neuAdj += amp
					elif fact[2] == "adverb" :
						neuAdv += amp
					elif fact[2] == "anypos":
						neuAny += amp

	return [posNoun, posVerb, posAdj, posAdv, posAny, negNoun, negVerb, negAdj, negAdv, negAny, neuNoun, neuVerb, neuAdj, neuAdv, neuAny]
