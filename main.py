import pygame
import random


# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Caption and icon
pygame.display.set_caption("Spacion Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.image.load("space-invaders.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 3
enemy_y_change = 40

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 8
bullet_state = "ready"


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# Game loop
running = True
while running:

    # Screen Background RGB
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -4
            if event.key == pygame.K_RIGHT:
                player_x_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    # Checking boundaries
    # Don't let spaceship go beyond the window
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_x_change

    # Don't let spaceship go beyond the window
    if enemy_x <= 0:
        enemy_x_change = 3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -3
        enemy_y += enemy_y_change

    # Bullet Movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
