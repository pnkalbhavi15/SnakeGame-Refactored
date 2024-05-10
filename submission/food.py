import random
from constants import DIS_WIDTH, DIS_HEIGHT, SNAKE_BLOCK, GREEN
from utils import *

class Food:
    def __init__(self, DIS):
        # Initialize the Food object with the given display surface
        self.DIS = DIS
        # Generate initial coordinates for the food
        self.x, self.y = self.generate_food()

    def generate_food(self):
        # Generate random coordinates for the food within the display boundaries
        foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
        foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
        return foodx, foody

    def draw(self):
        # Draw the food on the display surface
        pygame.draw.rect(self.DIS, GREEN, [self.x, self.y, SNAKE_BLOCK, SNAKE_BLOCK])
