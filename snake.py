#-- create a snake game in python
#-- using pygame
#-- by: @gillessuperr (github)
#-- 2023

import pygame
import random
import sys
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define some variables
block_size = 20
FPS = 10

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snake")

# Difine the initial direction of the snake
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Create a Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((size[0] / 2), (size[1] / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = cur[0], cur[1]

        if self.direction == UP:
            y -= block_size
        elif self.direction == DOWN:
            y += block_size
        elif self.direction == LEFT:
            x -= block_size
        elif self.direction == RIGHT:
            x += block_size

        self.positions.insert(0, (x, y))

        if len(self.positions) > self.length:
            self.positions.pop()

    def check_collision(self):
        if self.head_x < 0 or self.head_x >= width or self.head_y < 0 or self.head_y >= height:
            print("Game Over")
            pygame.quit()
            sys.exit()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (block_size, block_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = RIGHT


# Create a Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
    def randomize_position(self):
        self.position = (random.randint(0, size[0]/block_size - 1) * block_size, random.randint(0, size[1]/block_size - 1) * block_size)
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (block_size, block_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

# Initialize snake and food
snake = Snake()
food = Food()
food.randomize_position()

# Main game loop
while True:
    snake.handle_keys()
    snake.move()

    # Check for collision with food
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    # Fill screen with background color
    screen.fill(BLACK)

    # Draw snake and food
    snake.draw(screen)
    food.draw(screen)

    # Update display
    pygame.display.update()

    # Set frame rate
    clock = pygame.time.Clock()
    clock.tick(FPS)
