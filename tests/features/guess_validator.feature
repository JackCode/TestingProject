Feature: GuessValidator

    The GuessValidator checks various properties of the user's guess

    Scenario: Checking length of user guess
        Given the user enters TREE
        When the user presses Enter
        Then an error message is displayed

    Scenario: Check word is in dictionary

    Scenario: Correct response is received (-, *, letters)

    Scenario: Word is guessed correctly
