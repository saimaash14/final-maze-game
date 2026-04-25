# Final-Maze-Game

## Project Overview
This is a maze game where the player can select between two difficulty levels: Easy and Hard. The goal is to navigate a turtle through a maze, avoid walls, collect coins, and reach the end of the maze. The game keeps track of the player's lives, score, and displays win/lose screens.
## Key Features:
1. Turtle Movement: The player uses the arrow keys to move a turtle around the maze.
2. Difficulty Levels: There are two difficulty levels, Easy and Hard, which correspond to different maze layouts and numbers of lives.
3. Collision Detection: The player loses lives when colliding with the maze walls.
4. Coin Collection: The player collects coins scattered throughout the maze to increase their score.
5. Win and Lose Screens: The game provides feedback when the player wins or loses, and offers options to play again or quit.
6. Scoreboard: The score is updated every time a coin is collected, and the number of lives is displayed.
## What Each Section Does:
1. Setup Screen:
  The setup_screen() function sets up the initial screen, displaying a welcome message and a button to start the game.
2. Title Screen:
  The title_screen() function displays the title of the game and a button to start the game.
3. Level Selection Screen:
  The choose_level() function allows the player to choose between "Easy" and "Hard" levels by clicking buttons.
4. Maze Creation (Easy and Hard):
  The create_easy_maze() function reads from a file and draws the maze for the Easy level, creating walls and an endpoint.
  The create_hard_maze() function does the same for the Hard level but with different maze complexity.
5. Player Movement:
  The player can move the turtle using the arrow keys (up(), down(), right(), left() functions).
6. Collision Detection:
  The check_collision_easy() and check_collision_hard() functions check if the player has hit any walls and if so, reduces the player's lives.
7. Coin Collection:
  The draw_coin() function places coins on the maze grid, and coin_collision() checks if the player has collided with any coins.
8. Win and Lose Screens:
  The win_screen() and lose_screen() functions display a message depending on whether the player won or lost, and offer the option to try again or quit.
9. Scoreboard:
  The update_score() function updates and displays the player's current score and remaining lives.

## Tools & Technologies Used
Python – Core programming language used to build the game logic and structure. <br>
Turtle Graphics (Python Library) – Used to render the maze, player movement, coins, and visual elements on screen.

Live demo: https://youtu.be/Nn-JEjSi9jE?si=Kp6vvvjztQOzwHUH
