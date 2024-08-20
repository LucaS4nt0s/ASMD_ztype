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

inimigo_morto = False

def spawn_enemy():
    x = random.randint(0, screen_width - 55)
    y = random.randint(0, 100)

    return [x, y]


qtd_inimigos = [1, 2, 3, 5, 7]  # Define a quantidade de inimigos
enemy_speed = [0.5, 0.7, 1, 1.5, 1.75]  # Define a velocidade dos inimigos
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
    global inimigo_morto
    inimigo_morto = False   


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


def gera_operacao(numero1, numero2, operador):
    numero1 = random.randint(numeros[0], numeros[8])
    numero2 = random.randint(numeros[0], numeros[8])
    operador = random.choice(operadores)

    return numero1, numero2, operador

numero1 = 0
numero2 = 0
operador = '+'


numero1, numero2, operador = gera_operacao(numero1, numero2, operador)

resultado = str(eval(str(numero1) + operador + str(numero2)))
print(resultado)

input_rect = pygame.Rect((screen_width - 15) // 2, screen_height - 90, 140, 32)

# Game loop


def end_game():
    global running
    running = False
    pygame.quit()
    sys.exit()

def imprime_expressao(font):
    screen.blit(font.render(str(numero1) + ' ' + str(operador) + ' ' + str(numero2),
                    True, WHITE), ((screen_width - 70) // 2, (screen_height - 23) // 2))

lista_num = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

def game():
    fim_de_jogo = False
    global running
    global numero1, numero2, operador, resultado
    global inimigo_morto
    running = True
    user_input = ""
    resposta = ""
    score = 0
    font = pygame.font.Font('NewAmsterdam-Regular.ttf', 40)
    font2 = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)
    font_input = pygame.font.Font('NewAmsterdam-Regular.ttf', 23)
    get_pos_enemy_x = []
    get_pos_enemy_y = []
    for i in range(qtd_inimigos[0]):  # Começamos com a quantidade inicial de inimigos
        new_x, new_y = spawn_enemy()
        get_pos_enemy_x.append(new_x)
        get_pos_enemy_y.append(new_y)
        enemy_rect.append(enemy_image.get_rect())

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
            if event.type == pygame.QUIT:
                    end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # and len(user_input) > 0:
                    user_input = user_input[:-1]
                elif event.key in lista_num:
                    user_input += str(event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:
                    resposta = str(user_input)
                    print(resposta)
                    if resposta == str(resultado):
                        inimigo_morto = True
                        score += 1
                        print("Acertou")
                        numero1, numero2, operador = gera_operacao(numero1, numero2, operador)
                        resultado = eval(str(numero1) + operador + str(numero2))
                        if operador == '/' and resultado % 1 == 0:
                            resultado = round(resultado)
                        elif operador == '/':
                            resultado = round(resultado, 1)
                        imprime_expressao(font)
                        print(resultado)
                        resposta = ""
                    user_input = ""
                else:
                    user_input += event.unicode
                    
       

        # Draw the background
        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

        text_input = font_input.render(user_input, True, WHITE)
        screen.blit(text_input, (input_rect.x + 5, input_rect.y + 5))

        # Ajusta o tamanho da caixa de texto
        input_rect.w = max(50, text_input.get_width() + 10)

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
        inimigos_para_remover = []

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
        
        # Ajusta quantidade de inimigos ao score
        while len(get_pos_enemy_x) < qtd_inimigos[qtd_inimigos_por_score]:
            new_x, new_y = spawn_enemy()
            get_pos_enemy_x.append(new_x)
            get_pos_enemy_y.append(new_y)
            enemy_rect.append(enemy_image.get_rect())

        for i in range(len(get_pos_enemy_x)):

            enemy_rect[i].x = get_pos_enemy_x[i]
            enemy_rect[i].y = get_pos_enemy_y[i]

            if inimigo_morto:  # Verifique se inimigo_morto é True
                inimigos_para_remover.append(i)  # Marque o inimigo para remoção
                inimigo_morto = False

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

            # pygame.draw.rect(screen, (0, 0, 255), enemy_rect[i], 4)
            enemy(get_pos_enemy_x[i], get_pos_enemy_y[i], i)


            if collision(player_rect, enemy_rect[i]):
                fim_de_jogo = True
            
        for i in sorted(inimigos_para_remover, reverse=True):
            get_pos_enemy_x.pop(i)
            get_pos_enemy_y.pop(i)
            enemy_rect.pop(i)
            

        player_rect.x = (screen_width - 55) // 2
        player_rect.y = screen_height - 60

        # pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)

        pygame.display.flip()
        clock.tick(60)/1000


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
