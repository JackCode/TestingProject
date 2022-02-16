import sys
import os
import random

class Menu:
    def __init__(self) -> None:
        pass

    def show():
        clearScreen()
        print(
"""*** WORDLE Menu ****\n
1. View Instructions
2. Start new game
3. View game statistics
4. Exit""")
        return input("\nEnter your choice: ")

class Instructions:
    def show():
        clearScreen()
        print("""
*** Instructions ****

Guess the WORDLE in six tries!

Each guess must be a valid five-letter word. Press [enter] to submit.
After each guess, letters and symbols will be shown to show how close
your guess was to the word.

- means the letter is not found in the word
* means the letter is in the word but not in the correct position
if a letter is displayed, then the letter is in word and in the correct postion""")
        input("press [enter] to go back")

class Game:
    def __init__(self, words) -> None:
        self.words = words
        self.turnCount = 1

    def startNewGame(self):
        clearScreen()
        print("*** WORDLE ***\n")
        self.solution = self.getWordle()
        return self.run()

    def run(self):
        # unchanging solution
        permSolution = self.solution
        gameWon = False

        guesses = []
        gameSummary = []

        # start a game loop (6 turns)
        while (self.turnCount <= 6):
          print("Turn %d/6" %(self.turnCount))
          # store user guess
          guess = input("Guess:\t").upper()

          if guess == permSolution:
            clearScreen()
            print('You won with %d guess%s! The correct word was "%s"' %(self.turnCount, ('es','')[self.turnCount==1], permSolution))
            gameWon = True
            break

          if self.turnCount == 6 or guess == 'GIVE UP':
            clearScreen()
            print("Sorry, you lost. The correct word was '%s'\n" %(permSolution))
            break

          if len(guess) != 5:
            print("Guess must contain exactly 5 letters.\n")
            continue

          if guess not in self.words:
            print("Guess is not in dictionary\n")
            continue

          self.turnCount += 1

          # used to give results for each guess
          response = []
          # reset solution
          solution = permSolution
          guesses.append(guess)
          # loop through every letter in the guess
          for letterPosition in range(0, 5):
            # if the current letter in the guess is in the solution
            if guess[letterPosition] in solution:
              # if the letter is in the same place in guess and solution
              if letterPosition is solution.find(guess[letterPosition]):
                # mark with letter to indicate correct
                response.append(guess[letterPosition])
              # letter is in word, but wrong location
              else:
                # mark with star
                response.append('*')
              solution = solution.replace(guess[letterPosition], '-', 1)
            # letter is not in word
            else:
              response.append('-')

          resultStr = ''.join(response)
          gameSummary.append(resultStr)
          print("Result:\t%s\n" %(resultStr))

        for index in range(0,len(gameSummary)):
          print(guesses[index], "->", gameSummary[index])

        input("press [enter] to go back")

        return (gameWon, len(guesses))

    def getWordle(self):
        return random.choice(self.words).upper()

class Statistics:
    def __init__(self) -> None:
        pass

    def showStatistics():
        pass

    def writeStatistics(self, results):
        print("writing results: ", results[0], results[1])
        input()


class Wordle:
    def __init__(self) -> None:
        self.stats = Statistics()

    def loadDictionary(self, wordListFile = './wordle/wordle_list.txt'):
        self.words = open(wordListFile).read().upper().splitlines()

    def runGame(self):
        while True:
            self.choice = Menu.show()
            self.menuChoice(self.choice)
    
    def menuChoice(self, choice):
        match choice:
                case '1':
                    Instructions.show()
                case '2':
                    newGame = Game(self.words)
                    self.stats.writeStatistics(newGame.startNewGame())
                case '3':
                    self.stats.showStatistics()
                case '4':
                    sys.exit()


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__=="__main__":
    wordle = Wordle()
    wordle.loadDictionary()
    wordle.runGame()
