import pygame
from constants import *

# Initialize Pygame font module
pygame.font.init()

# Set up font for messages
try:
    FONT_STYLE = pygame.font.SysFont("Arial", 50)  # Change "Arial" to any valid font name installed on your system
except pygame.error:
    print("Error: Font not available. Defaulting to system font.")  
    FONT_STYLE = pygame.font.SysFont(None, 50)

def message(DIS, msg, color):
    """Display a message on the screen."""
    mesg = FONT_STYLE.render(msg, True, color)
    DIS.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def game_over_screen(DIS):
    """Display the game over screen."""
    DIS.fill(BLUE)  # Fill the display with a blue background
    message(DIS, "Game Over! Press C to Play Again or Q to Quit", RED)  # Display game over message
    pygame.display.update()  # Update the display

def handle_events(DIS, snake):
    """Handle game events such as keyboard input."""
    for event in pygame.event.get():  # Loop through each Pygame event
        if event.type == pygame.QUIT:  # If the user clicks the close button
            pygame.quit()  # Quit Pygame
            quit()  # Exit the program
        if event.type == pygame.KEYDOWN:  # If a key is pressed
            # Change snake direction based on arrow key input
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
