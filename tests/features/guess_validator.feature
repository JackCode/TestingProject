Feature: GuessValidator

    The GuessValidator checks various properties of the user's guess

    Scenario Outline: Checking length of user guess
        Given the player enters <word>
        When the player submits their guess
        Then an error message <is_isnot> displayed

        Examples: 
        | word    | is_isnot |
        | tree    | is       |
        | grasp   | isnot    |
        | mansion | is       |

    Scenario Outline: Checking guess is correct/incorrect

        Given the game has started and has <solution>
        And the player has typed <guess>
        When the player presses enter
        Then the guess is marked as <correct_or_incorrect>

        Examples:
        | solution | guess   | correct_or_incorrect |
        | shale    | shale   | correct              |
        | radio    | carrz   | incorrect            |
        | grasp    | grasp   | correct              |
        | vague    | vagui   | incorrect            |

    Scenario Outline: Checking valid word is in dictionary
        Given the player enters <word>
        And the game has a <dictionary> of valid words
        When the player types enter
        Then an error message <is_isnot> displayed

        Examples:
        | word   | dictionary    | is_isnot |
        | one     | one two three | isnot       |
        | two     | one two three | isnot       |
        | three   | one two three | isnot       |
        | four    | one two three | is    |
        | our     | four five six | is    |

    # Scenario Outline: Correct response is received (-, *, letters)
    #     Given the player enters a <valid guess>
    #     When the game has a <solution>
    #     Then the response received is <response>

    #     Examples: Valid Guesses
    #     | BIKES | BIKES | BIKES |

    # Scenario: Word is guessed correctly
