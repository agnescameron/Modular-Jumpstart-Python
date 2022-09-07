import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

article=open("article.txt", "r")
text = article.read()
tokens = word_tokenize(text)
tags = pos_tag(tokens)

print(tags)

names = []
nouns = []

for tag in tags:
	if tag[1] == "NN":
		nouns.append(tag[0])
	elif tag[1] == "NNP":
		names.append(tag[0])


print("names:")
print(names)

print("\n")

print("nouns:")
print(nouns)