import sys
import os
import random

class Menu:
    def __init__(self) -> None:
        pass

    def show():
        #clearScreen()
        print(
"""*** WORDLE Menu ****\n
1. View Instructions
2. Start new game
3. View game statistics
4. Exit""")
        return input("\nEnter your choice: ")

class Instructions:
    def show():
        #clearScreen()
        print("""*** Instructions ****

Guess the WORDLE in six tries!

Each guess must be a valid five-letter word. Press [enter] to submit.
After each guess, letters and symbols will be shown to show how close
your guess was to the word.

- means the letter is not found in the word
* means the letter is in the word but not in the correct position
if a letter is displayed, then the letter is in word and in the correct postion\n""")

class Game:
    def __init__(self, words) -> None:
        self.words = words

    def startNewGame(self):
        #clearScreen()
        print("*** WORDLE ***\n")
        self.solution = self.getWordle()
        return self.run()

    def run(self):
        validator = GuessValidator(self.solution, "", "")
        # unchanging solution
        permSolution = self.solution
        gameWon = False

        guesses = []
        gameSummary = []

        # start a game loop (6 turns)
        while (len(guesses) < 6):
            print("Turn %d/6" %(len(guesses)+1))
            # store user guess
            guess = input("Guess:\t").upper()
            validator.guess = guess

            if not validator.checkCorrectLength():
                print(validator.message)
                continue

            if not validator.checkGuessInDictionary(self.words):
                print(validator.message)
                continue

            guesses.append(guess)

            if guess == 'GIVE UP':
                print("\nSorry, you lost. The correct word was '%s'\n" %(permSolution))
                break
        
            resultStr = ''.join(validator.getGuessResponse(self.solution, guess))

            gameSummary.append(resultStr)
            print("Result:\t%s\n" %(resultStr))

            if len(guesses) == 6 and guess != 'GIVE UP':
                #clearScreen()
                print("\nSorry, you lost. The correct word was '%s'\n" %(permSolution))
                break

            if guess == permSolution:
                #clearScreen()
                print('\nYou won with %d guess%s! The correct word was "%s"' %(self.turnCount, ('es','')[self.turnCount==1], permSolution))
                gameWon = True
                break

        for index in range(0,len(gameSummary)):
            print(guesses[index], "->", gameSummary[index])

        print('')
        return gameWon

    def getWordle(self):
        return random.choice(self.words).upper()

class GuessValidator:
    def __init__(self, solution, guess, message) -> None:
        self.solution = solution
        self.guess = guess
        self.message = message

    def checkCorrectLength(self):
        if len(self.guess) != 5:
            self.message = "Guess must contain exactly 5 letters.\n"
            return False
        self.message = ""
        return True

    def checkGuessInDictionary(self, wordList):
        if self.guess not in wordList:
            self.message = "Guess is not in dictionary\n"
            return False
        self.message = ""
        return True

    def checkGuessIsCorrect(self):
        return self.guess == self.solution

    def getGuessResponse(self, solution, guess):
        self.solution = solution
        self.guess = guess
        
        # used to give results for each guess
        response = []
        
        # loop through every letter in the guess
        for letterPosition in range(0, 5):
        # if the current letter in the guess is in the solution
            if self.guess[letterPosition] in self.solution:
                # if the letter is in the same place in guess and solution
                if letterPosition is self.solution.find(self.guess[letterPosition]):
                    # mark with letter to indicate correct
                    response.append(self.guess[letterPosition])
                # letter is in word, but wrong location
                else:
                    # mark with star
                    response.append('*')
                    self.solution = self.solution.replace(self.guess[letterPosition], '-', 1)
            # letter is not in word
            else:
                response.append('-')
        return response


            
# just record number of wins and losses
class Statistics:
    def __init__(self) -> None:
        pass

    def showStatistics():
        pass

    def writeStatistics(self, results):
        pass


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
