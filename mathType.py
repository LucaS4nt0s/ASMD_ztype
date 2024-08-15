import pygame
import random

"""
INICIO DO NOSSO PROJETO DE PROJETO DE EXTENSÃO 2
"""
# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the background
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

pygame.display.set_caption("ASMD Game")

# Set up the player character
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (55, 55))
player_rect = player_image.get_rect()
player_rect.centerx = screen_width // 2
player_rect.bottom = screen_height - 10

# Set up the enemy characters
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (55, 55))
enemy_rects = []
enemy_speed = 0.2

enemy_spawn_delay = 1000  # Delay between enemy spawns in milliseconds
last_spawn_time = pygame.time.get_ticks()  # Get the current time

# Function to spawn a new enemy
def spawn_enemy():
    enemy_rect = enemy_image.get_rect()
    enemy_rect.x = random.randint(0, screen_width - enemy_rect.width)
    enemy_rect.y = -enemy_rect.height
    enemy_rects.append(enemy_rect)

    # Game loop
    running = True
    while running:
        # ...

        # Check if it's time to spawn a new enemy
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time >= enemy_spawn_delay:
            spawn_enemy()
            last_spawn_time = current_time

        # ...


# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ...

    # Draw the background
    screen.blit(background_image, (0, 0))

    # ...
    
    # Update player position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5


    # Update enemy positions
    for enemy_rect in enemy_rects:
        if enemy_rect.y < player_rect.y:
            enemy_rect.y += enemy_speed
        if enemy_rect.x < player_rect.x:
            enemy_rect.x += enemy_speed
        if enemy_rect.x > player_rect.x:
            enemy_rect.x -= enemy_speed
    pygame.display.flip()

# Quit the game
pygame.quit()


