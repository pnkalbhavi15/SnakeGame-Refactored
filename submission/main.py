import pygame
from constants import *
from snake import Snake
from food import Food
from utils import *

# Initialize Pygame
pygame.init()

# Set up the display
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game by Edureka')

# Set up the clock
CLOCK = pygame.time.Clock()

def game_loop():
    """Main game loop."""
    game_over = False
    snake = Snake(DIS)  # Initialize the snake object with the display surface
    food = Food(DIS)    # Initialize the food object with the display surface

    while not game_over:
        handle_events(DIS, snake)  # Handle user input events

        snake.move()  # Move the snake

        # Check for collisions with itself or the boundaries
        if snake.check_collision() or snake.check_boundary():
            game_over = True

        # Check if the snake has eaten the food
        if snake.x == food.x and snake.y == food.y:
            # Regenerate food at a new location and increase the snake's length
            food.x, food.y = food.generate_food()
            snake.increase_length()

        DIS.fill(BLUE)  # Clear the display surface with a blue background
        food.draw()     # Draw the food on the display surface
        snake.draw()    # Draw the snake on the display surface

        # Maintain the snake's movement history for updating its length
        snake.snake_list.append([snake.x, snake.y])
        if len(snake.snake_list) > snake.length_of_snake:
            del snake.snake_list[0]

        pygame.display.update()  # Update the display
        CLOCK.tick(SNAKE_SPEED)  # Control the game speed

    # Display the game over screen
    game_over_screen(DIS)
    
    # Handle events after game over
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:  # Restart the game
                    game_loop()

# Start the game loop
if __name__ == "__main__":
    game_loop()
