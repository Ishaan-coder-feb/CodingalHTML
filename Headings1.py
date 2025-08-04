import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Pygame Example")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Player settings
player_size = 50
x = 100
y = 100
speed = 5

# Clock for FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
screen.fill(white)

# Event loop
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False

# Get keys pressed
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
x -= speed
if keys[pygame.K_RIGHT]:
x += speed
if keys[pygame.K_UP]:
y -= speed
if keys[pygame.K_DOWN]:
y += speed

# Draw red square
pygame.draw.rect(screen, red, (x, y, player_size, player_size))

pygame.display.update()
clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()