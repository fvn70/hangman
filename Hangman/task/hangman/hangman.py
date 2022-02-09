import random

lives = 8
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
puzzle = '-' * len(word)
print("H A N G M A N")
while lives:
    print()
    print(puzzle)
    ch = input("Input a letter: ")
    if ch in word:
        if ch in puzzle:
            print("No improvements")
            lives -= 1
        else:
            for i in range(len(word)):
                if word[i] == ch:
                    puzzle = puzzle[:i] + ch + puzzle[i + 1:]
            if puzzle == word:
                print("You guessed the word!")
                print("You survived!")
                break
    else:
        lives -= 1
        print("That letter doesn't appear in the word")

if not lives:
    print("You lost!")
