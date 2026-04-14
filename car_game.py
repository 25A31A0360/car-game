import pygame
import random

# 1. Setup & Constants
pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Dodger")

# Colors
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
WHITE = (255, 255, 255)

# Game Variables
car_width, car_height = 50, 80
player_x = WIDTH // 2 - car_width // 2
player_y = HEIGHT - 100
player_speed = 8

enemy_width, enemy_height = 50, 80
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -100
enemy_speed = 5

score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# 2. Main Game Loop
running = True
while running:
    SCREEN.fill(GRAY) # Draw the road
    
    # Event Handling (Check for closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - car_width:
        player_x += player_speed

    # 4. Enemy Logic
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(0, WIDTH - enemy_width)
        score += 1
        enemy_speed += 0.2 # Make it harder over time

    # 5. Collision Detection
    player_rect = pygame.Rect(player_x, player_y, car_width, car_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    if player_rect.colliderect(enemy_rect):
        print(f"Game Over! Final Score: {score}")
        running = False

    # 6. Drawing Everything
    pygame.draw.rect(SCREEN, BLUE, player_rect)  # Player
    pygame.draw.rect(SCREEN, RED, enemy_rect)    # Enemy
    
    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip() # Update the screen
    clock.tick(60) # 60 Frames Per Second

pygame.quit()