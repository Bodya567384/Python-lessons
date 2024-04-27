import pygame
import random

IMAGES_PATH: str = 'images/'
screen_width: int = 601
screen_height: int = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Wizard:
    x: int = 0
    y: int = 500
    width: int = 0
    height: int = 0
    speed: int = 10
    image_name: str = '1_IDLE_000.png'
    image = None
    image_left = None
    image_right = None

    def __init__(self):
        self.image_right = pygame.image.load(IMAGES_PATH + self.image_name)
        self.image = self.image_right
        self.image_left = pygame.transform.flip(self.image_right, 180, 0)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = int(screen_width / 2 - self.width / 2)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction: str):
        if direction == 'left':
            self.image = self.image_left
            self.move_left()
        elif direction == 'right':
            self.image = self.image_right
            self.move_right()
    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x + self.speed <= screen_width - self.width:
            self.x += self.speed
        else:
            self.x = screen_width - self.width


class SuperWizard(Wizard):
    max_y = 500
    count_jump = 0
    def __init__(self):
        super().__init__()

    def move(self, direction):
        if direction == 'left':
            self.image = self.image_left
            self.move_left()
        elif direction == 'right':
            self.image = self.image_right
            self.move_right()

        if self.y < self.max_y:
            self.y += 2

        if self.y >= self.max_y:
            self.count_jump = 0

    def jump(self):
        if self.count_jump < 2:
            self.y -= 100
            self.count_jump += 1


class Diamond:
    x: int = 0
    y: int = 0
    speed: int = 0
    image: None

    def __init__(self, image):
        self.image = image
        w = self.image.get_width()
        self.x = random.randint(0, screen_width - w)
        self.speed = random.randint(2, 5)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def fall(self):
        self.y += self.speed

class Diamonds:
    diamonds_images: list = []
    diamonds_list: list = []

    def __init__(self):
        self.load_images()

    def load_images(self):
        images = ('8.png', '9.png', '11.png',)
        for i in images:
            self.diamonds_images.append(pygame.image.load(IMAGES_PATH + i))

    def add(self):
        img = self.diamonds_images[random.randint(0, len(self.diamonds_images)-1)]
        self.diamonds_list.append(Diamond(img))

    def draw(self):
        for item in self.diamonds_list:
            item.show()

    def fall(self):
        for item in self.diamonds_list:
            item.fall()

    def player_collision(self, player):
        collision = 0
        for item in self.diamonds_list:
            if item.y > screen_height:
                collision = -1
                self.diamonds_list.remove(item)
            if ((item.x > player.x and item.x < player.x + player.width) and
                    (item.y > player.y and item.y < player.y + player.height)):
                collision = 1
                self.diamonds_list.remove(item)


        return collision


class Game:
    run: bool = True
    fps: int = 60
    clock = pygame.time.Clock()
    background = None
    player = Wizard
    player_move: str = ''
    diamonds: Diamonds
    diamond_event = pygame.USEREVENT + 1
    player_catch: int = 0
    player_lost: int = 0

    def __init__(self):
        pygame.display.set_caption('Wizard')
        self.background_add(IMAGES_PATH + 'background.png')

        self.player = SuperWizard
        self.player = Wizard

        self.player = SuperWizard()
        self.diamonds = Diamonds()
        self.diamonds_add()

    def diamonds_add(self):
        # Timer
        pygame.time.set_timer(self.diamond_event, 1000)
        self.diamonds.add()

    def background_add(self, image: str):
        self.background = pygame.image.load(image)

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.background, xy)

    def check_collision(self):
        check = self.diamonds.player_collision(self.player)

        if check == 1:
            self.player_catch += 1
        elif check == -1:
            self.player_lost += 1

    def game_status(self):
        self.check_collision()

        font = pygame.font.SysFont('Arial', 30)
        t = f' Score {self.player_catch} - {self.player_lost} '
        text = font.render(t, True, (255, 255, 255), (47, 14, 51))
        screen.blit(text, (10, 10))

    def play(self):
        while self.run:
            # 1: check event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player_move = 'left'
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player_move = 'right'
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:

                        self.player.jump()
                elif event.type == pygame.KEYUP:
                    self.player_move = ''
                elif event.type == self.diamond_event:
                    self.diamonds_add()

            if self.run:
                self.background_draw()
                self.player.move(self.player_move)
                self.diamonds.fall()
                self.player.show()
                self.diamonds.draw()
                self.game_status()


                pygame.display.update()
                self.clock.tick(self.fps)
        # === end while ===

        pygame.quit()


g = Game()
g.play()