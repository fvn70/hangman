import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
puzzle = '-' * len(word)
print("H A N G M A N")
for _ in range(8):
    print()
    print(puzzle)
    ch = input("Input a letter: ")
    if ch in word:
        for i in range(len(word)):
            if word[i] == ch:
                puzzle = puzzle[:i] + ch + puzzle[i + 1:]
    else:
        print("That letter doesn't appear in the word")

print("\nThanks for playing!")
print("We'll see how well you did in the next stage")
