poem = open("roastbeef.txt", "r") 

lines = poem.readlines()


# split up the words
for line in lines:
	# use the split method to split the line into single words
	words = line.split(' ')
	for word in words:
		print(word)


# add in numbers
for line in lines:
	# use the split method to split the line into single words
	words = line.split(' ')
	for index, word in enumerate(words):
		print(index, word)