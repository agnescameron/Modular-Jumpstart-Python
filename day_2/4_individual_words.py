poem = open("roastbeef.txt", "r") 

lines = poem.readlines()


print('\n##############  1\n')

# split up the words
for line in lines:
	# use the split method to split the line into single words
	words = line.split(' ')
	for word in words:
		print(word)

print('\n##############  2\n')

# add in numbers
for line in lines:
	# use the split method to split the line into single words
	words = line.split(' ')
	for index, word in enumerate(words):
		print(index, word)


print('\n##############  3\n')

# use the numbers for things!
for line in lines:
	# use the split method to split the line into single words
	words = line.split(' ')
	for index, word in enumerate(words):
		for i in range(0, index):
			print(' ', end='')
		print(word)