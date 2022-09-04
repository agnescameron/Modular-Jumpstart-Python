# printing using loops

for i in range (0, 10):
	print('#')

# let's see what's happening in i
for i in range (0, 10):
	print(i)

# print a grid -- this will print one line 10 times

# grid no1
print('\n')
print('grid number 1')
for i in range (0, 10):
	print('##########')


# make it look a bit more griddy
# grid no2
print('\n')
print('grid number 2')
for i in range (0, 10):
	print('|#|#|#|#|#|#|#|#|#|#|')

# use 2 for loops to print a grid
print('\n')
print('grid number 3')
for i in range (0, 10):
	for j in range (0, 10):
		print('|#', end='')
	print('')


# use the value of i
print('\n')
print('pyramid 1')
for i in range (0, 10):
	for j in range (0, i):
		print('|#', end='')
	print('')

# changing direction
print('\n')
print('pyramid 1')
for i in range (0, 10):
	for j in range (0, 10-i):
		print('|#', end='')
	print('')



# triple nesting!
for x in range (0, 10):
	for i in range (0, x):
		for j in range (0, i):
			print('|#', end='')
		print('')

	for i in range (0, x):
		for j in range (0, x-i):
			print('|#', end='')
		print('')



