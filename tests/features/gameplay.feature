Feature: Gameplay

  Showing various gameplay scenarios

  Scenario Outline: Viewing Unsuccessful Gameplay
    Given user enters <userGuesses> when correct word is <correctWord>
    Then user sees the message you lost
    Examples:
      | userGuesses                             | correctWord |
      | point,train,scent,water,straw,punch     | fraud       |

  Scenario Outline: Viewing Successful Gameplay
    Given user enters <userGuesses> when correct word is <correctWord>
    Then user see the message you won
    Examples:
      | userGuesses                             | correctWord |
      | point,train,scent,water,straw,punch     | straw       |