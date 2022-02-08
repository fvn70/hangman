import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
print("H A N G M A N")
if input("Guess the word: ") == word:
    print("You survived!")
else:
    print("You lost!")
