import time
import random
import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGES_PATH = 'images/'
FPS: int = 1000

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player():
    pass

class Game:
    background_image = None

    def __init__(self):
        self.interval = time.time()
        self.dt = 1
        self.add_background()

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

    def add_background(self):
        i = random.randint(1, 2)
        self.background_image = pygame.image.load(IMAGES_PATH + f'grass{i}.png')
        nx = int(SCREEN_WIDTH / self.background_image.get_width()) + 1
        ny = int(SCREEN_HEIGHT / self.background_image.get_height()) + 1
        for x in range(nx):
            for y in range(ny):
                screen.blit(self.background_image, (250 * x, 250 * y))

    def init(self):
        while True:
            self.delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.init()
