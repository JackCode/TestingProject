from cgi import test
import sys
import os
import random

testing = False
wins = losses = 0

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
        if testing:
            return

class Game:
    def __init__(self, words) -> None:
        self.words = words

    def startNewGame(self):
        #clearScreen()
        print("*** WORDLE ***\n")
        if testing:
            return
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

            if guess != 'GIVE UP' and not validator.checkCorrectLength():
                print(validator.message)
                continue

            if guess != 'GIVE UP' and not validator.checkGuessInDictionary(self.words):
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
                print('\nYou won with %d guess%s! The correct word was "%s"' %(len(guesses), ('es','')[len(guesses)==1], permSolution))
                gameWon = True
                break

        for index in range(0,len(gameSummary)):
            print(guesses[index], "->", gameSummary[index])

        print('')
        global wins, losses
        if gameWon:
            wins += 1
        else:
            losses += 1
        return

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

        result = ['-', '-', '-', '-', '-']
        for i in range(0, 5):
            if guess[i] == solution[i]:
                result[i] = guess[i]

        for i in range(0, 5):
            for j in range(0, 5):
                
                if guess[i] == solution[j] and result[i] == '-':
                    result[i] = '*'
        return result
# just record number of wins and losses
class Statistics:
    def __init__(self) -> None:
        pass

    def showStatistics(self):
        print('*** Statistics ***\n')
        if testing:
            return

        global wins, losses
        print("Number of Recorded Wins:", wins)
        print("Number of Recorded Loses:", losses)
        if wins + losses > 0:
            percentage = wins/(wins+losses)
        else:
            percentage = 0
        print('Win Percentage: %d%%\n' % percentage)

    def resetStats():
        global wins, losses
        wins = losses = 0


class Wordle:
    def __init__(self, stdout_mock=sys.__stdout__, testModeNoGame=False) -> None:
        # if flag is true, only text for each section is displayed
        # prevents game from running when option 2 is selected
        global testing
        testing = testModeNoGame
        # used to redirect stdout for testing purposes
        sys.stdout = stdout_mock
        self.stats = Statistics()

    def loadDictionary(self, wordListFile = './wordle/wordle_list.txt'):
        self.words = open(wordListFile).read().upper().splitlines()

    def runGame(self):
        while True:
            self.choice = Menu.show()
            print('\n')
            self.menuChoice(self.choice)
            
    
    def menuChoice(self, choice):
        match choice:
                case '1':
                    Instructions.show()
                case '2':
                    newGame = Game(self.words)
                    newGame.startNewGame()
                case '3':
                    self.stats.showStatistics()
                case '4':
                    sys.exit()


if __name__=="__main__":
    wordle = Wordle()
    wordle.loadDictionary()
    wordle.runGame()
