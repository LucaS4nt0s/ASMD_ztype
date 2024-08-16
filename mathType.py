import pygame
import random
import math

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
background_image = pygame.transform.scale(
    background_image, (screen_width, screen_height))

pygame.display.set_caption("ASMD Game")

# Set up the player character
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (55, 55))


# Set up the enemy characters
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (55, 55))

# Get the rect of the player and enemy (used for collision detection)
player_rect = player_image.get_rect()
enemy_rect = enemy_image.get_rect()

# def text_objects(text, font):
#     textSurface = font.render(text, True, (255, 255, 255))
#     background_image.blit(textSurface, ((screen_width - textSurface.get_width()) // 2, (screen_height - textSurface.get_height()) // 2))
# Function to spawn a new enemy


def spawn_enemy():
    x = random.randint(0, screen_width - 55)
    y = random.randint(0, 100)

    return [x, y]


def collision(player, enemy):
    if player.colliderect(enemy):
        return True
    else:
        return False


# Get the initial enemy position


# Game loop
def game():
    running = True
    fim_de_jogo = False
    get_pos_enemy_x = spawn_enemy()[0]
    get_pos_enemy_y = spawn_enemy()[1]
    font = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)
    while running:
        while fim_de_jogo:

            game_over_text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, ((screen_width - game_over_text.get_width()) // 2, (screen_height - game_over_text.get_height() - 50) // 2))

            play_again_text = font.render("Aperte ESPACO para jogar novamente ou a tecla S para sair", True, (255, 255, 255))
            screen.blit(play_again_text, ((screen_width - play_again_text.get_width()) //2, (screen_height - play_again_text.get_height() - 50) // 2 + 50))

            pygame.display.flip()
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    fim_de_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        fim_de_jogo = False
                        game()
                    elif event.key == pygame.K_s:
                        running = False
                        fim_de_jogo = False
                        pygame.quit()
        # ...

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Draw the background
        screen.blit(background_image, (0, 0))

        screen.blit(enemy_image, (get_pos_enemy_x, get_pos_enemy_y))

        screen.blit(
            player_image, ((screen_width - 55) // 2, screen_height - 60))

        enemy_rect.x = get_pos_enemy_x
        enemy_rect.y = get_pos_enemy_y

        player_rect.x = (screen_width - 55) // 2
        player_rect.y = screen_height - 60

        pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
        pygame.draw.rect(screen, (0, 0, 255), enemy_rect, 4)

        # Calculate the direction vector from enemy to player
        direction_x = player_rect.x - enemy_rect.x
        direction_y = player_rect.y - enemy_rect.y

        # Normalize the direction vector
        direction_length = math.sqrt(direction_x ** 2 + direction_y ** 2)
        direction_x /= direction_length
        direction_y /= direction_length

        # Set the enemy speed
        enemy_speed = 0.02

        # Update the enemy position based on the direction vector
        get_pos_enemy_x += direction_x * enemy_speed
        get_pos_enemy_y += direction_y * enemy_speed
        enemy_rect.x = get_pos_enemy_x
        enemy_rect.y = get_pos_enemy_y

        # Check for collision
        if collision(player_rect, enemy_rect):
            fim_de_jogo = True

        pygame.display.flip()


# Start the game
game()

# Quit the game
pygame.quit()
