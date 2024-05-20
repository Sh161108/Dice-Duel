# Snakes and Ladders Dice Game

This project is a simple implementation of the classic Snakes and Ladders game with dice rolling. Players can choose to play either against another player or the computer.

## Game Modes

1. **Player vs Player (P_Vs_P)**
2. **Player vs Computer (P_Vs_C)**

## How to Play

- Players take turns rolling a dice to advance their position on the board.
- Landing on a ladder allows the player to move up to a higher position.
- Landing on a snake causes the player to slide down to a lower position.
- The first player to reach or exceed position 100 wins the game.

## Features

- Snakes and Ladders are predefined.
- Dice roll is randomized between 1 and 6.
- Scores are updated after each roll.
- Interactive prompts for user input.

## Running the Game

1. Run the script.
2. Choose the game mode.
3. Follow the prompts to roll the dice and advance on the board.

## Code Explanation

The game logic is divided into two main functions:
- `PlayerVsComp`: Handles the gameplay for Player vs Computer mode.
- `PlayerVsPlayer`: Handles the gameplay for Player vs Player mode.

The game uses dictionaries to store the positions of snakes and ladders. It updates the player's or computer's score based on dice rolls and checks for any interactions with snakes or ladders.

## Example

```plaintext
You want to play in which mode? (P_Vs_P / P_Vs_C) P_Vs_C
Roll the dice (y/n)? y
Player rolled: 4
Computer rolled: 6

Player's Score: 4
Computer's Score: 6

Roll the dice (y/n)? y
Player rolled: 3
Computer rolled: 2

Player's Score: 7
Computer's Score: 8
...
