import time

poem = open("roastbeef.txt", "r") 

# we can read all the lines in the file into a list

lines = poem.readlines()

# here's our list
print(lines)

time.sleep(1)

print('\n')

# we can use a for loop to go over each item
for line in lines:
	print(line)
	time.sleep(1)
