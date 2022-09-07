from textblob import TextBlob

statement = input("give me an opinion: ")
opinion = TextBlob(statement)

print(opinion.sentiment)

if opinion.sentiment.polarity > 0.1:
	print("seems pretty positive!")

elif opinion.sentiment.polarity < -0.1:
	print("hm, that's a shame")

else:
	print("can't say either way")