Feature: Gameplay

  Showing various gameplay scenarios

  Scenario Outline: Viewing Guess Options
    Given user enters a guess <userGuess>
    When user submits the guess
    Then user sees the option to enter word
    Examples:
      | userGuess |
      | point     |
