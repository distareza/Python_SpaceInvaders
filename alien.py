from turtle import Turtle, Screen
from alien_bullet import AlienBullet

class Alien(Turtle):

    ALIEN_SPEED = 1
    ALIEN_FORWARD_DIRECTION = True

    def __init__(self, sc:Screen, model:int, x:int, y:int):
        super().__init__()
        alien = f"images/alien_ship_{model}_small.gif"
        sc.register_shape(alien)
        self.shape(alien)
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.bullet = None

    def hide(self):
        self.penup()
        self.goto(999999,999999)
        self.pendown()

    def fire(self):
        if self.bullet is None:
            self.bullet = AlienBullet()
            print(self.xcor(), self.ycor())
            self.bullet.move(self.xcor(), self.ycor())

    def bullet_move(self):
        if self.bullet is not None:
            self.bullet.fire()
            if self.bullet.isOutOfRange():
                self.bullet.hide()
                self.bullet = None

    def move(self):
        if self.ALIEN_FORWARD_DIRECTION:
            self.forward(self.ALIEN_SPEED)
        else:
            self.backward(self.ALIEN_SPEED)

