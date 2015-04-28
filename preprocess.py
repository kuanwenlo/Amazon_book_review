import math
from xml.dom import minidom

posdoc = minidom.parse("positive.review")
negdoc = minidom.parse("negative.review")

pos_reviews = posdoc.getElementsByTagName('review_text')
neg_reviews = negdoc.getElementsByTagName('review_text')

posReviews = []
negReviews = []

for review in pos_reviews:
	posReviews.append(review.firstChild.data)
for review in neg_reviews:
	negReviews.append(review.firstChild.data)

print posReviews


