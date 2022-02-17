from behave import *
from wordle.core import *

@given(u'user enters a guess {userGuess}')
def step_impl(context,userGuess):
    context.wordle.userGuess = userGuess

@when(u'user submits the guess')
def step_impl(context):
    with open('./tests/features/output.txt', 'w') as f:
        context.wordle = Wordle(f, True)
        context.wordle.loadDictionary()
        context.wordle.menuChoice('2')

@then(u'user sees the option to enter word')
def step_impl(context):
    with open('./tests/features/output.txt', 'r') as f:
        assert f.readline().find('Turn 1/6') > -1
