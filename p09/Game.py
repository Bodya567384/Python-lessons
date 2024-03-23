import pygame
import random

pygame.init()

#Screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Color
black = (0, 0, 0)  # RGB
white = (255, 255, 255)
game_over = False

# pokemon
pokemon = pygame.image.load('images/jigglypuff.png')
pokemon_size = 70
pokemon_x = random.randint(0, screen_width - pokemon_size)
pokemon_y = random.randint(0, screen_height - pokemon_size)

#cursor
cursor_picture = pygame.image.load('images/pokemon_ball.png')
pygame.mouse.set_visible(False)

clock_fps = 60
clock = pygame.time.Clock()

current_fps = 0
font_style = pygame.font.SysFont('Gabriola', 30)

def cursor_draw(picture):
    position = pygame.mouse.get_pos()
    x = position[0] - 40
    y = position[1] - 40
    screen.blit(picture, (x, y))

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pass

    screen.fill(black)
    screen.blit(pokemon, (pokemon_x, pokemon_y))
    cursor_draw(cursor_picture)

    current_fps = clock.get_fps()
    fps_text = font_style.render(f'{current_fps: .1f}', True, white)
    screen.blit(fps_text, (screen_width - 50,10 ))

    pygame.display.flip()
    clock.tick(clock_fps)

pygame.quit()