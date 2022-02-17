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

    # Scenario: Check word is in dictionary

    # Scenario: Correct response is received (-, *, letters)

    # Scenario: Word is guessed correctly
