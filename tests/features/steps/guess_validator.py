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
    