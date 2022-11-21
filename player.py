from turtle import Turtle, Screen
from player_bullet import PlayerBullet

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -270)
MAX_RIGHT = 280
MIN_LEFT = -280

class Player(Turtle):

    def __init__(self, sc:Screen):
        super().__init__()
        alien = f"images/Player_small.gif"

        sc.register_shape(alien)
        self.shape(alien)
        self.penup()
        self.goto(STARTING_POSITION)
        self.pendown()
        self.bullet = []

    def right(self):
        if self.pos()[0] < MAX_RIGHT:
            self.penup()
            self.forward(MOVE_DISTANCE)
            self.pendown()


    def left(self):
        if self.pos()[0] > MIN_LEFT:
            self.penup()
            self.backward(MOVE_DISTANCE)
            self.pendown()

    def fire(self):
        bullet = PlayerBullet()
        print(self.xcor(), self.ycor())
        bullet.move(self.xcor(), self.ycor())
        self.bullet.append(bullet)

    def bullet_move(self):
        for bullet in self.bullet:
            bullet.fire()
            if bullet.isOutOfRange():
                self.bullet.remove(bullet)
