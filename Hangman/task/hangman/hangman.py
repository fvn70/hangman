import random
import re


class Game:
    lives = 8
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    puzzle = '-' * len(word)
    w_set = set()

    def read_char(self):
        while self.lives:
            print()
            print(self.puzzle)
            ch = input("Input a letter: ")
            if len(ch) != 1:
                print("You should input a single letter")
            elif not re.match('[a-z]', ch):
                print("Please enter a lowercase English letter")
            elif ch in self.w_set:
                print("You've already guessed this letter")
            else:
                self.w_set.add(ch)
                break
        return ch

    def play(self):
        while self.lives:
            ch = self.read_char()
            if ch in self.word:
                if ch in self.puzzle:
                    print("No improvements")
                    self.lives -= 1
                else:
                    for i in range(len(self.word)):
                        if self.word[i] == ch:
                            self.puzzle = self.puzzle[:i] + ch + self.puzzle[i + 1:]
                    if self.puzzle == self.word:
                        print("You guessed the word!")
                        print("You survived!")
                        break
            else:
                self.lives -= 1
                print("That letter doesn't appear in the word")

        if not self.lives:
            print("You lost!")


game = Game()
print("H A N G M A N")
while True:
    cmd = input('Type "play" to play the game, "exit" to quit: ')
    if cmd == "play":
        game.play()
        print()
    elif cmd == "exit":
        break

