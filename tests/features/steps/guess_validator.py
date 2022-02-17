from behave import *

from wordle.core import GuessValidator

@given(u'the user enters TREE')
def step_impl(context):
    context.guess = 'TREE'


@when(u'the user presses Enter')
def step_impl(context):
    gv = GuessValidator("", context.guess, "")
    context.response = gv.checkCorrectLength()


@then(u'an error message is displayed')
def step_impl(context):
    assert context.response is False