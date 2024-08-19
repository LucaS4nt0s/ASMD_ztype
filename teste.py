#faça um código com a biblioteca pygame que permita ler um numero digitado pelo usuário e imprima na tela o número digitado

import pygame
import random
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

# Set up the enemy characters
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (55, 55))
enemy_img = []
enemy_rect = []
for i in range(10):  # Gera 10 inimigos
    # Adiciona a imagem do inimigo na lista de imagens de inimigos
    enemy_img.append(enemy_image)
    enemy_rect.append(enemy_image.get_rect())
# Get the rect of the player and enemy (used for collision detection)
player_rect = player_image.get_rect()

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))



#function to read the number typed by the user
def read_number():
    number = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    number += "0"
                elif event.key == pygame.K_1:
                    number += "1"
                elif event.key == pygame.K_2:
                    number += "2"
                elif event.key == pygame.K_3:
                    number += "3"
                elif event.key == pygame.K_4:
                    number += "4"
                elif event.key == pygame.K_5:
                    number += "5"
                elif event.key == pygame.K_6:
                    number += "6"
                elif event.key == pygame.K_7:
                    number += "7"
                elif event.key == pygame.K_8:
                    number += "8"
                elif event.key == pygame.K_9:
                    number += "9"
                elif event.key == pygame.K_RETURN:
                    return int(number)
                elif event.key == pygame.K_BACKSPACE:
                    number = number[:-1]
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render(number, True, BLACK)
        screen.blit(text, (100, 100))
        pygame.display.update()
        clock.tick(60)


# Game loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (screen_width / 2 - 25, screen_height - 100))

    for i in range(10):
        enemy_rect[i].y += 2
        if enemy_rect[i].y > screen_height:
            enemy_rect[i].y = random.randint(-200, -50)
            enemy_rect[i].x = random.randint(0, screen_width - 55)
        enemy(enemy_rect[i].x, enemy_rect[i].y, i)

    pygame.display.update()

    number = read_number()
    print(number)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
