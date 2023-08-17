#25000 words
import random

f = open('data.txt', 'r')
f_content = f.read()

#words = {}
#for count in range(25000):
#    words[count] = 10
f_contents = f_content.split(',')
print(f_contents[0])


word_choice = random.choice(f_contents).lstrip()
print(word_choice)
print(len(word_choice))

#Random number goes to f_contents to get random word