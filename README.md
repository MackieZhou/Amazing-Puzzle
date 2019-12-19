### THE AMAZING PUZZLE
The final project for CSC 111  
Mackie Zhou, Grace Li, Winnie Zong  
Group 11

### How to play the game?
1. Run the main.py file to play the game.
1. A python package, pygame, needs to be installed. See [pygame official website](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation) to learn how to pip install pygame.

### Game Description
Bored by problem sets and papers? Here come the **ultimate crazy puzzles**!!! Choose a difficult level and challenge yourself!
1. **How to win?**
    - Cover the two static grey squares by the two colored squares at the same time, and you win!
1. **How to play?**
    - Firstly, you want to choose a **difficult level**. You have difficult level 9, 99, and 999 to choose from.
    - Secondly, play! Control the movement of the red square and the blue square by hitting the **left, right, up, or down arrow keys** on your keyboard. Each keyboard hit has effect on both colored squares, though it's possible that only one square will move.
1. **Any rules?**
    - Unfortunately, you **cannot move across a wall**. (If there's a wall on the left side of the red square and you hit the left arrow key, the red square won't move!) It means you may get into a situation where one square moves, but the other does not.
    - Pay attention to the numbers around the arena. If you **move a colored square out** of the arena from one side of a tile, the colored square will **come back** into the arena from the other tile that has **the same number** marked next to it.
    - The two colored squares **must not overlap**.
