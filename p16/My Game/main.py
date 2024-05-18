import sys

import pygame
import random
import time

SCREEN_WIDTH = 260 * 3  # 780
SCREEN_HEIGHT = 260 * 2  # 520
IMAGES_PATH_BG = 'images/'
IMAGES_PATH_MENU = 'images/menu/'
FONT_PATH = 'fonts'
FPS: int = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player:
    pass

class Background:
    image = None

    def __init__(self):
        self.bg_x: int = 0
        self.bg_y: int = -SCREEN_HEIGHT
        self.bg_y_speed: float = 0.8
        self.bg_y_position = self.bg_y
        self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2))

        self.add()

    def add(self):
        i = random.randint(1, 2)
        self.image = pygame.image.load(IMAGES_PATH_BG + 'bg01.png')

        nx = int(SCREEN_WIDTH / self.image.get_width())
        ny = int(SCREEN_HEIGHT / self.image.get_height())
        w = self.image.get_width()
        h = self.image.get_height()

        for x in range(nx):
            for y in range(ny * 2):
                self.bg_surface.blit(self.image, (w * x, h * y))

    def draw(self):
        self.bg_y_position += self.bg_y_speed
        self.bg_y = int(self.bg_y_position)

        if self.bg_y >= 0:
            self.bg_y = -SCREEN_HEIGHT
            self.bg_y_position = self.bg_y

        screen.blit(self.bg_surface, (self.bg_x, self.bg_y))

class Menu:
    def __init__(self):
        bg_img = pygame.image.load(IMAGES_PATH_MENU + 'bg-03.jpg')
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        box_img = pygame.image.load(IMAGES_PATH_MENU + 'Window.png')
        self.box_img = pygame.transform.scale(box_img, (300, 300))

    def start_button(self):
        color = (0, 0, 0)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if self.start_pos():
            color = (255, 255, 255)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        font = pygame.font.SysFont(FONT_PATH + 'Oswald-VariableFont_wght.ttf', 50)
        text = font.render('START', True, color)
        screen.blit(text, (335, 120))

    def draw(self):
        screen.blit(self.bg_img, (0, 0))
        screen.blit(self.box_img, (int(SCREEN_WIDTH / 2 - self.box_img.get_width() / 2), 20))
        self.start_button()

    def start_pos(self):
        pos = pygame.mouse.get_pos()
        print(pos)

        if ((pos[0] > 320 and pos[0] < 400) and (pos[1] > 120 and pos[1] < 140)):
            return True

        return False
    def click_mouse(self):
        btn = pygame.mouse.get_pressed() # (False, False, False)

        if btn[0] and self.start_pos():
            return 'run'

        return None


class Game:
    game_run: bool = False

    def __init__(self):
        pygame.display.set_caption('StarFly')
        self.interval = time.time()
        self.dt = 1
        self.menu = Menu()
        self.bg = Background()
        self.player = Player()


    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

    def init(self):
        self.game_run = True

        while self:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu.click_mouse() == 'run':
                        self.run()

            self.menu.draw()
            pygame.display.update()

    def run(self):
        self.game_run = True

        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_run = False

            self.bg.draw()
            # TODO: ігровий процес
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.init()
