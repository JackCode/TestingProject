from behave import *

from wordle.core import *

@given(u'the user enters a valid value of {menuchoice}')
def step_impl(context, menuchoice):
    context.choice = menuchoice
    
@when(u'the user submits the choice')
def step_impl(context):
    with open('./tests/features/output.txt', 'w') as f:
        context.wordle = Wordle(f, True)
        context.wordle.loadDictionary()
        context.wordle.menuChoice(context.choice)

@then(u'the game will display {screen}')
def step_impl(context, screen):
    with open('./tests/features/output.txt', 'r') as f:
        assert f.readline().find(screen) > -1
