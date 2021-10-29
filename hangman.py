import random
import re

def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    size = len(word)
    hide = list("-" * size)
    w_set = set()
    cnt = 8

    while cnt > 0:
        print()
        print(''.join(hide))
        ch = input("Input a letter: ")
        if len(ch) != 1:
            print("You should input a single letter")
            continue
        if not re.match('[a-z]', ch):
            print("Please enter a lowercase English letter")
            continue
        if ch in w_set:
            print("You've already guessed this letter")
            continue
        else:
            w_set.add(ch)
        if ch in hide:
            print("No improvements")
            cnt -= 1
            continue
        if word.count(ch) > 0:
            for i in range(size):
                if word[i] == ch:
                    hide[i] = ch
            if word == ''.join(hide):
                break
        else:
            print("That letter doesn't appear in the word")
            cnt -= 1
    if cnt > 0:
        print("You survived!")
    else:
        print("You lost!")

print("H A N G M A N")

while True:
    cmd = input('Type "play" to play the game, "exit" to quit: ')
    if cmd == "play":
        game()
        print()
    elif cmd == "exit":
        break
