import io
from sys import stdin
from behave import *
import pyautogui

from wordle.core import *

@given(u'the user enters a valid value of {menuchoice}')
def step_impl(context, menuchoice):
    context.choice = menuchoice
    
@when(u'the user submits the choice')
def step_impl(context):
    context.wordle = Wordle()
    context.wordle.loadDictionary()
    context.wordle.menuChoice(context.choice)

@then(u'the game will display {screen}')
def step_impl(context, screen):
    pass
