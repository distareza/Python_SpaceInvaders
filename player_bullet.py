from turtle import Turtle

PLAYER_BULLET_WIDTH = 2
PLAYER_BULLET_HEIGHT = .2
BULLET_SPEED = 15

class PlayerBullet(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.shapesize(PLAYER_BULLET_HEIGHT, PLAYER_BULLET_WIDTH)
        self.color("red")
        self.setheading(90)

    def move(self, X, Y):
        self.penup()
        self.goto(X, Y)
        self.pendown()

    def fire(self):
        self.penup()
        self.forward(BULLET_SPEED)
        self.pendown()

    def isOutOfRange(self):
        return self.ycor() > 1000

    def hide(self):
        self.penup()
        self.goto(999999,999999)
        self.pendown()