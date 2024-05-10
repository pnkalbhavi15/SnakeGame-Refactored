import random
from constants import DIS_WIDTH, DIS_HEIGHT, SNAKE_BLOCK, BLACK
from utils import *

class Snake:
    def __init__(self, DIS):
        # Initialize the snake with the given display surface
        self.DIS = DIS
        # Initialize the snake's properties
        self.snake_list = []  # List to store the coordinates of each segment of the snake
        self.length_of_snake = 1  # Initial length of the snake
        self.x, self.y = DIS_WIDTH / 2, DIS_HEIGHT / 2  # Initial position of the snake
        # Randomly choose initial direction for the snake
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.score = 0  # Initialize score to track the player's progress

    def move(self):
        # Move the snake in its current direction
        if self.direction == "UP":
            self.y -= SNAKE_BLOCK
        elif self.direction == "DOWN":
            self.y += SNAKE_BLOCK
        elif self.direction == "LEFT":
            self.x -= SNAKE_BLOCK
        elif self.direction == "RIGHT":
            self.x += SNAKE_BLOCK

    def draw(self):
        # Draw each segment of the snake on the display surface
        for segment in self.snake_list:
            pygame.draw.rect(self.DIS, BLACK, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def increase_length(self):
        # Increase the length of the snake when it eats food and update the score
        self.length_of_snake += 1
        self.score += 1

    def check_collision(self):
        # Check if the snake collides with itself
        if [self.x, self.y] in self.snake_list[:-1]:
            return True
        return False

    def check_boundary(self):
        # Check if the snake hits the boundaries of the display
        if self.x >= DIS_WIDTH or self.x < 0 or self.y >= DIS_HEIGHT or self.y < 0:
            return True
        return False
