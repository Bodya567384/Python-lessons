# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

# ініціалізація бібліотеки (запустити)
pygame.init()
# створити екран
screen = pygame.display.set_mode((800, 600))
# заголовок вікна
pygame.display.set_caption('Good-Boy')
# обмеження частоти оновлення екрану
clock = pygame.time.Clock()
clock_tick = 60
# завантажуємо зображення
spyder_img = pygame.image.load('images/spyder.png')
spyder_position = {'x': 0, 'y': 0}

while True:
    # перевіряємо події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        spyder_position['y'] -= 3
    if keys[pygame.K_s]:
        spyder_position['y'] += 3
    if keys[pygame.K_d]:
        spyder_position['x'] += 3
    if keys[pygame.K_a]:
        spyder_position['x'] -= 3

    # 1. додаємо об'єкти на екран
    screen.blit(spyder_img, (spyder_position['x'], spyder_position['y']))


    # 2. оновлюємо екран
    pygame.display.update()
    # обмеження частоти оновлення - limit FPS
    clock.tick(clock_tick)