Feature: Menu

    Showing operation of menu to navigate various functionality of program

    Scenario Outline: Viewing Screens
        Given the user enters a valid value of <menuchoice>
        When the user submits the choice
        Then the game will display <screen>

        Examples: Choices
           | menuchoice    | screen        |
           | 1             | Instructions  |
           #| 2             | WORDLE        |
           #| 3             | Statistics    |