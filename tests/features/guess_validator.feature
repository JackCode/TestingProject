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

    Scenario Outline: Correct response is received (-, *, letters)
        Given the player enters a <valid guess>
        When the game has a <solution>
        Then the response received is <response>

        Examples: Valid Guesses
        | BIKES | BIKES | BIKES |

    # Scenario: Word is guessed correctly
