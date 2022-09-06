# this uses the termcolor library, 
# which you will need to download -- 
# we haven't got to libraries yet, but if you're interested,
# you can try installing the library by running the following command:
# python3 -m pip install termcolor
# cprint and colored are 2 functions that we are importing from termcolor

from termcolor import colored, cprint

text = colored('i am red and flashing', 'red', attrs=['blink'])
print(text)
cprint('I like to have green background', 'red', 'on_green')