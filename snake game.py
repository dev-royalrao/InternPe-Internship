import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 450  # Increase the width and height
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # Change border color to black
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # Change score color to blue
GREEN = (0, 255, 0)  # Change snake color to green

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)

# Initialize the food
food = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))  # Avoid border

# Game variables
score = 0
game_over = False

# Initialize the font for scoring and game over
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1) and snake[0][1] > 0:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1) and snake[0][1] < GRID_HEIGHT - 1:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0) and snake[0][0] > 0:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0) and snake[0][0] < GRID_WIDTH - 1:
                snake_direction = (1, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Check if the snake hits the wall
    if (
        new_head[0] < 0
        or new_head[0] >= GRID_WIDTH
        or new_head[1] < 0
        or new_head[1] >= GRID_HEIGHT
    ):
        game_over = True

    # Check for collisions with itself
    if new_head in snake:
        game_over = True

    # Check if the snake eats the food
    if new_head == food:
        score += 1
        food = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))  # Avoid border
    else:
        snake.pop()

    # Add the new head to the snake
    snake.insert(0, new_head)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the borders
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, GRID_SIZE))  # Top border
    pygame.draw.rect(screen, BLACK, (0, 0, GRID_SIZE, HEIGHT))  # Left border
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - GRID_SIZE, WIDTH, GRID_SIZE))  # Bottom border
    pygame.draw.rect(screen, BLACK, (WIDTH - GRID_SIZE, 0, GRID_SIZE, HEIGHT))  # Right border

    # Draw the food
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the snake (changed color to green)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Display the score (top-middle and blue)
    score_text = font.render(f"Score: {score}", True, BLUE)
    score_rect = score_text.get_rect()
    score_rect.midtop = (WIDTH // 2, GRID_SIZE)  # Adjusted position
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Game over
game_over_text = game_over_font.render("Game Over", True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH // 2, HEIGHT // 2 - 36)  # Position the "Game Over" text
screen.blit(game_over_text, game_over_rect)

final_score_text = font.render(f"Your Score: {score}", True, BLUE)
final_score_rect = final_score_text.get_rect()
final_score_rect.midtop = (WIDTH // 2, HEIGHT // 2 + 36)  # Position the final score text
screen.blit(final_score_text, final_score_rect)

pygame.display.update()

# Wait for a moment before quitting (3 seconds)
pygame.time.delay(3000)

pygame.quit()
sys.exit()
