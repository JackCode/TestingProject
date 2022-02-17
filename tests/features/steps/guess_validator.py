from behave import *

from wordle.core import GuessValidator

@given(u'the player enters {word}')
def step_impl(context, word):
    context.guess = word


@when(u'the player submits their guess')
def step_impl(context):
    gv = GuessValidator("", context.guess, "")
    context.response = gv.checkCorrectLength()


@then(u'an error message {is_isnot} displayed')
def step_impl(context, is_isnot):
    if is_isnot == 'is':
        assert context.response is False
    else:
        assert context.response is True
    

@given(u'the game has started and has {solution}')
def step_impl(context, solution):
    context.solution = solution


@given(u'the player has typed {guess}')
def step_impl(context, guess):
    context.guess = guess


@when(u'the player presses enter')
def step_impl(context):
    gv = GuessValidator(context.solution, context.guess, "")
    context.response = gv.checkGuessIsCorrect()


@then(u'the guess is marked as {correct_or_incorrect}')
def step_impl(context, correct_or_incorrect):
    if correct_or_incorrect == 'correct':
        assert context.response is True
    else:
        assert context.response is False

@given(u'the game has a {dictionary} of valid words')
def step_impl(context, dictionary):
    context.dictionary = dictionary.split()


@when(u'the player types enter')
def step_impl(context):
    gv = GuessValidator("", context.guess, "")
    context.response = gv.checkGuessInDictionary(context.dictionary)