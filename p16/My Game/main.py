import sys

import pygame
import random
import time

SCREEN_WIDTH = 780
SCREEN_HEIGHT = 780
IMAGES_PATH = 'images/'
FPS: int = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player:
    player_image = pygame.image.load(IMAGES_PATH + 'Ship1.png')

class Background:
    pass

class Game:
    background_image = None
    game_run: bool = False

    def __init__(self):
        self.bg_x: int = 0
        self.bg_y: int = -SCREEN_HEIGHT
        self.bg_y_speed: float = 0.8
        self.bg_y_position = self.bg_y
        self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2))

        self.interval = time.time()
        self.dt = 1

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

    def add_background(self):
        i = random.randint(1, 2)
        self.background_image = pygame.image.load(IMAGES_PATH + 'bg01.png')

        nx = int(SCREEN_WIDTH / self.background_image.get_width())
        ny = int(SCREEN_HEIGHT / self.background_image.get_height())
        w = self.background_image.get_width()
        h = self.background_image.get_height()

        for x in range(nx):
            for y in range(ny * 2):
                self.bg_surface.blit(self.background_image, (w * x, h * y))

    def draw_background(self):
        self.bg_y_position += self.bg_y_speed
        self.bg_y = int(self.bg_y_position)

        if self.bg_y >= 0:
            self.bg_y = -SCREEN_HEIGHT
            self.bg_y_position = self.bg_y

        screen.blit(self.bg_surface, (self.bg_x, self.bg_y))

    def menu(self):
        im = pygame.image.load(IMAGES_PATH + 'bg_menu.jpg')
        screen.blit(im, (0, 0))

        font = pygame.font.SysFont('Calibri', 40)
        mes = 'S'
        text = font.render(mes, True, 'White')
        screen.blit(text, (300, 120))


    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

            self.menu()
            pygame.display.update()

    def run(self):
        self.game_run = True
        self.add_background()

        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_run = False

            self.draw_background()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.init()
