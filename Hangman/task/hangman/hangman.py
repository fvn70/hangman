import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
print("H A N G M A N")
if input(f"Guess the word {word[:3]}{'-' * (len(word) - 3)}: ") == word:
    print("You survived!")
else:
    print("You lost!")
