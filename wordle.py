#@title
import random

#globalStats = [0]*6
globalStats = [1,1,5,6,3,2]
numOfGamesPlayed = 20
numOfSuccessfulGuesses = 18
def getInstructions():
    print(""" *** Instructions ****
                    1)word should be 5 letters
                    2)you have only 6 guesses to find the correct word
                    3)- means letter not found in the word
                    4) * means letter in the word but not in correct position
                    5)if letter is displayed then letter is in word and it is in corect postion""")

def startNewGame():
  # load dictionary from file
  # case all words to upper case
  global numOfGamesPlayed, numOfSuccessfulGuesses, globalStats
  numOfGamesPlayed += 1
  words = open('wordle_list.txt').read().upper().splitlines()

  # choose random word from word list as solution
  solution = random.choice(words).upper()

  # variable to track turns
  turnCount = 1

  # unchanging solution
  permSolution = solution

  guesses = []
  gameSummary = []

  # start a game loop (6 turns)
  while (turnCount <= 6):
    print("Turn %d/6" %(turnCount))
    # store user guess
    guess = input("Guess:\t").upper()

    if guess == permSolution:
      print('You won with %d guess%s! The correct word was "%s"' %(turnCount, ('es','')[turnCount==1], permSolution))
      globalStats[turnCount] += 1
      numOfSuccessfulGuesses += 1
      break

    if len(guess) != 5:
      print("Guess must contain exactly 5 letters.\n")
      continue

    if guess not in words:
      print("Guess is not in dictionary\n")
      continue

    if turnCount == 6 or guess == 'GIVE UP':
      print("Sorry, you lost. The correct word was '%s'" %(permSolution))
      break

    turnCount += 1

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

  print("")

def statistics():
  winPercentage = (numOfSuccessfulGuesses/numOfGamesPlayed) * 100
  print ( "Number of Games played %d, successful guesses %d and Win Percentage %d " %(numOfGamesPlayed, numOfSuccessfulGuesses, winPercentage ))
  for stat in range(0, len(globalStats)):
    print( "No. of times you guessed the word in %d chance %d" %(stat+1,globalStats[stat]))

while True :
    print("""Welcome to Wordle
        Menu
        1. View Instructions
        2. Start new game
        3. View game statistics
        4. Exit""")
    menuIndex = input("enter your choice: ")
    if menuIndex == '1':
      getInstructions()
      continue
    elif menuIndex == '2':
      startNewGame()
      continue
    elif menuIndex == '3':
      statistics()
    elif menuIndex == '4':
      print("Exit")
      break
      