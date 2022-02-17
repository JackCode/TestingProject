from behave import *
from wordle.core import *

@given(u'user enters {userGuesses} when correct word is {correctWord}')
def step_impl(context, correctWord, userGuesses):
    with open('./tests/features/output.txt', 'w') as f:
        context.wordle = Wordle(f, True)
        context.wordle.loadDictionary()
        context.wordle.newGame = Game(context.wordle.words)
        context.wordle.newGame.solution = correctWord.upper()
        context.wordle.newGame.userGuesses = userGuesses.split(',')
        context.wordle.newGame.run()

@then(u'user sees the message you lost')
def step_impl(context):
    with open('./tests/features/output.txt', 'r') as f:
        assert f.read().find("Sorry, you lost. The correct word was '" + context.wordle.newGame.solution + "'") > -1

@then(u'user see the message you won')
def step_impl(context):
    with open('./tests/features/output.txt', 'r') as f:
        output = f.read()
        assert output.find("You won with") > -1
        assert output.find('The correct word was "' + context.wordle.newGame.solution + '"')