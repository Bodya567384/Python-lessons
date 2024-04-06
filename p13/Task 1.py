import random

# x_1dd_00d: int = 12
# _dd_f: str = "12"

class Ball:
    MAX_X = 100
    color: tuple = (0, 0, 0)
    radius: int = 0
    weight: float = 0
    speed: int = 0
    x: int = 0
    y: int = 0

    def __init__(self, radius: int, weight: float):
        if radius > 0:
            self.radius = radius
        else:
            print('Error! Radius cannot equal/less zero')
        self.weight = weight
        print('!!! Start !!!')

    def movement(self):...

    def mov_x(self, speed_x: int = 0):...

    def mov_y(self, speed_x: int = 0):...


ball_1 = Ball(-2,20)
ball_1.speed = 5

ball_1.mov_x()
ball_1.mov_x(40)
ball_1.mov_x()
# for i in range(5):
#     ball_1.speed = random.randint(0, 10)
#     print(ball_1.speed)
#     ball_1.movement()

print(ball_1.x, ball_1.y)
