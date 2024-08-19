import pygame
import random
import math
import sys

"""
INICIO DO NOSSO PROJETO DE PROJETO DE EXTENSÃO 2
"""
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

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
background_image = pygame.transform.scale(
    background_image, (screen_width, screen_height))

pygame.display.set_caption("ASMD Game")

# Set up the player character
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (55, 55))


def spawn_enemy():
    x = random.randint(0, screen_width - 55)
    y = random.randint(0, 100)

    return [x, y]


qtd_inimigos = [1, 2, 3, 5, 7]  # Define a quantidade de inimigos
enemy_speed = [0.5, 1, 1.5, 2, 2.5]  # Define a velocidade dos inimigos
# Set up the enemy characters
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (55, 55))
enemy_img = []
enemy_rect = []
for i in range(qtd_inimigos[4]):  # Gera 10 inimigos
    # Adiciona a imagem do inimigo na lista de imagens de inimigos
    enemy_img.append(enemy_image)
    enemy_rect.append(enemy_image.get_rect())
# Get the rect of the player and enemy (used for collision detection)
player_rect = player_image.get_rect()


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def imprimirCX(text, font, cor, y):  # Função para imprimir texto no centro da tela em x
    textSurface = font.render(text, True, cor)
    screen.blit(textSurface, ((screen_width - textSurface.get_width()) // 2, y))
# Function to spawn a new enemy


def collision(player, enemy):
    if player.colliderect(enemy):
        return True
    else:
        return False


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
operadores = ['+', '-', '*', '/']


def gera_operacao(numero1, numero2, operador, font):
    numero1 = random.randint(numeros[0], numeros[8])
    numero2 = random.randint(numeros[0], numeros[8])
    operador = random.choice(operadores)

    return numero1, numero2, operador


numero1 = 0
numero2 = 0
operador = '+'

numero1, numero2, operador = gera_operacao(
    numero1, numero2, operador, pygame.font.Font('NewAmsterdam-Regular.ttf', 35))

input_rect = pygame.Rect((screen_width - 15) // 2, screen_height - 90, 140, 32)

# Game loop


def end_game():
    running = False
    pygame.quit()
    sys.exit()


def game():
    fim_de_jogo = False
    running = True
    user_input = ""
    score = 40
    font = pygame.font.Font('NewAmsterdam-Regular.ttf', 40)
    font2 = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)
    font_input = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)
    get_pos_enemy_x = []
    get_pos_enemy_y = []
    for i in range(qtd_inimigos[4]):  # Gera 10 inimigos
        get_pos_enemy_x.append(spawn_enemy()[0])
        get_pos_enemy_y.append(spawn_enemy()[1])
    while running:
        while fim_de_jogo:
            screen.blit(background_image, (0, 0))
            imprimirCX("Fim de jogo", font, RED, (screen_height // 2) - 100)
            imprimirCX("Pressione espaço para jogar novamente", font2,
                       BLACK, (screen_height // 2) - 50)
            imprimirCX("Pressione ESC para sair", font2,
                       BLACK, (screen_height // 2) - 20)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game()
                    elif event.key == pygame.K_ESCAPE:
                        end_game()
        # ...

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # and len(user_input) > 0:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_0:
                    user_input += "0"
                elif event.key == pygame.K_1:
                    user_input += "1"
                elif event.key == pygame.K_2:
                    user_input += "2"
                elif event.key == pygame.K_3:
                    user_input += "3"
                elif event.key == pygame.K_4:
                    user_input += "4"
                elif event.key == pygame.K_5:
                    user_input += "5"
                elif event.key == pygame.K_6:
                    user_input += "6"
                elif event.key == pygame.K_7:
                    user_input += "7"
                elif event.key == pygame.K_8:
                    user_input += "8"
                elif event.key == pygame.K_9:
                    user_input += "9"
                elif event.key == pygame.K_RETURN:
                    return str(user_input)
                else:
                    user_input += event.unicode

        # Draw the background
        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

        text_input = font_input.render(user_input, True, WHITE)
        screen.blit(text_input, (input_rect.x + 5, input_rect.y + 5))

        # Ajusta o tamanho da caixa de texto
        input_rect.w = max(100, text_input.get_width() + 10)

        # Imprime o score
        screen.blit(font2.render(
            "Score: " + str(score), True, WHITE), (10, 10))

        screen.blit(font.render(str(numero1) + ' ' + str(operador) + ' ' + str(numero2),
                    True, WHITE), ((screen_width - 70) // 2, (screen_height - 23) // 2))

        screen.blit(
            player_image, ((screen_width - 55) // 2, screen_height - 60))

        direction_x = []
        direction_y = []
        direction_length = []

        qtd_inimigos_por_score = 0
        enemy_speed_por_score = 0

        if score < 3:
            qtd_inimigos_por_score = 0
            enemy_speed_por_score = 0
        elif score < 9:
            qtd_inimigos_por_score = 1
            enemy_speed_por_score = 1
        elif score < 18:
            qtd_inimigos_por_score = 2
            enemy_speed_por_score = 2
        elif score < 32:
            qtd_inimigos_por_score = 3
            enemy_speed_por_score = 3
        else:
            qtd_inimigos_por_score = 4
            enemy_speed_por_score = 4

        for i in range(qtd_inimigos[qtd_inimigos_por_score]):

            enemy_rect[i].x = get_pos_enemy_x[i]
            enemy_rect[i].y = get_pos_enemy_y[i]

            # Calculate the direction vector from enemy to player

            direction_x.append(player_rect.x - enemy_rect[i].x)
            direction_y.append(player_rect.y - enemy_rect[i].y)

            # Normalize the direction vector

            direction_length1 = math.sqrt(
                direction_x[i] ** 2 + direction_y[i] ** 2) + 0.0001
            direction_length.append(direction_length1)
            direction_x[i] /= direction_length[i]
            direction_y[i] /= direction_length[i]

            # Update the enemy position based on the direction vector
            get_pos_enemy_x[i] += direction_x[i] * \
                enemy_speed[enemy_speed_por_score]
            get_pos_enemy_y[i] += direction_y[i] * \
                enemy_speed[enemy_speed_por_score]
            enemy_rect[i].x = get_pos_enemy_x[i]
            enemy_rect[i].y = get_pos_enemy_y[i]

            pygame.draw.rect(screen, (0, 0, 255), enemy_rect[i], 4)
            enemy(get_pos_enemy_x[i], get_pos_enemy_y[i], i)

            if collision(player_rect, enemy_rect[i]):
                fim_de_jogo = True

        player_rect.x = (screen_width - 55) // 2
        player_rect.y = screen_height - 60

        pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)

        pygame.display.flip()
        clock.tick(60)


# Start the game
def start_game():
    running = True
    while running:
        font = pygame.font.Font('NewAmsterdam-Regular.ttf', 40)
        font2 = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)

        screen.blit(background_image, (0, 0))

        imprimirCX("ASMD Game", font, WHITE, (screen_height // 2) - 100)
        imprimirCX("Pressione espaço para começar", font2,
                   WHITE, (screen_height // 2) - 50)

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
