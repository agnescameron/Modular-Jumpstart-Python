poem = open("roastbeef.txt", "r") 

# we can read all the lines in the file into a list

lines = poem.readlines()

print('\n##############  1\n')

# we can use a for loop to go over each item
for line in lines:
	new_line = line.replace('beef', 'chicken')
	print(new_line)

print('\n##############  2\n')

# what about multiple replacements
for line in lines:
	new_line = line.replace('beef', 'chicken').replace('sincere', 'severe').replace('please', 'hurt')
	print(new_line)

print('\n##############  3\n')

# what about lower case
for line in lines:
	new_line = line.lower().replace('beef', 'chicken').replace('sincere', 'severe').replace('please', 'hurt')
	print(new_line)
