import pygame
import random
import math

"""
INICIO DO NOSSO PROJETO DE PROJETO DE EXTENSÃO 2
"""
# Initialize Pygame
pygame.init()

# Set up color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

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

def spawn_enemy():
    x = random.randint(0, screen_width - 55)
    y = random.randint(0, 100)

    return [x, y]

qtd_inimigos = 10 # Define a quantidade de inimigos
# Set up the enemy characters
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (55, 55))
enemy_img = []
enemy_rect = []
for i in range(qtd_inimigos): # Gera 10 inimigos
    enemy_img.append(enemy_image) # Adiciona a imagem do inimigo na lista de imagens de inimigos
    enemy_rect.append(enemy_image.get_rect())
# Get the rect of the player and enemy (used for collision detection)
player_rect = player_image.get_rect()

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def imprimirCX(text, font, cor, y): # Função para imprimir texto no centro da tela em x
    textSurface = font.render(text, True, cor)
    screen.blit(textSurface, ((screen_width - textSurface.get_width()) // 2, y))
# Function to spawn a new enemy


def collision(player, enemy):
    if player.colliderect(enemy):
        return True
    else:
        return False


# Game loop
def game():
    fim_de_jogo = False
    running = True
    font = pygame.font.Font('NewAmsterdam-Regular.ttf', 40)
    font2 = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)
    get_pos_enemy_x = []
    get_pos_enemy_y = []
    for i in range(qtd_inimigos): # Gera 10 inimigos
        get_pos_enemy_x.append(spawn_enemy()[0])
        get_pos_enemy_y.append(spawn_enemy()[1])
    while running:
        while fim_de_jogo:
            imprimirCX("Fim de jogo!", font, RED, (screen_height // 2) - 100)
            imprimirCX("Pressione espaço para jogar novamente ou ESC para sair", font2, WHITE, (screen_height // 2) - 50)

            pygame.display.flip()
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    fim_de_jogo = False
                    pygame.quit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        fim_de_jogo = False
                        game()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        fim_de_jogo = False
                        pygame.quit()
                        
                        
        # ...
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fim_de_jogo = False
                pygame.quit()
          

        # Draw the background
        screen.blit(background_image, (0, 0))

        screen.blit(player_image, ((screen_width - 55) // 2, screen_height - 60))

        direction_x = []
        direction_y = []
        direction_length = []

        for i in range(qtd_inimigos):

            enemy_rect[i].x = get_pos_enemy_x[i]
            enemy_rect[i].y = get_pos_enemy_y[i]

            # Calculate the direction vector from enemy to player
            
            direction_x.append(player_rect.x - enemy_rect[i].x)
            direction_y.append(player_rect.y - enemy_rect[i].y)

            # Normalize the direction vector
            
            direction_length1 = math.sqrt(direction_x[i] ** 2 + direction_y[i] ** 2) + 0.0001
            direction_length.append(direction_length1)
            direction_x[i] /= direction_length[i]
            direction_y[i] /= direction_length[i]

            # Set the enemy speed
            enemy_speed = 0.1

            # Update the enemy position based on the direction vector
            get_pos_enemy_x[i] += direction_x[i] * enemy_speed
            get_pos_enemy_y[i] += direction_y[i] * enemy_speed
            enemy_rect[i].x = get_pos_enemy_x[i]
            enemy_rect[i].y = get_pos_enemy_y[i]

            pygame.draw.rect(screen, (0, 0, 255), enemy_rect[i], 4)
            enemy(get_pos_enemy_x[i], get_pos_enemy_y[i], i)

            if collision(player_rect, enemy_rect[i]):
                fim_de_jogo = True

        player_rect.x = (screen_width - 55) // 2
        player_rect.y = screen_height - 60

        pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)


        # Check for collision
        

        pygame.display.flip()


# Start the game
def start_game():
    running = True
    while running:
        font = pygame.font.Font('NewAmsterdam-Regular.ttf', 40)
        font2 = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)

        screen.blit(background_image, (0, 0))

        imprimirCX("ASMD Game", font, WHITE, (screen_height // 2) - 100)
        imprimirCX("Pressione espaço para começar", font2, WHITE, (screen_height // 2) - 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        pygame.display.flip()

start_game()

# Quit the game
pygame.quit()

