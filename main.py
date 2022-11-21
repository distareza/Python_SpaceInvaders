from turtle import Turtle, Screen
import random
import time
from scoreboard import Scoreboard
from alien import Alien
from player import Player

screen_width:int = 600
screen_height:int = 600

# setup screen
screen = Screen()
screen.setup(screen_width + 20, screen_height + 20)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)
screen.listen()

# Wall
box = Turtle()
box.color("red")
box.hideturtle()
box.penup()
box.goto(-screen_width / 2 + 2, screen_height / 2 - 2)
box.pendown()
box.goto(screen_width / 2 - 2, screen_height / 2 - 2)
box.goto(screen_width / 2 - 2, -screen_height / 2 + 2)
box.goto(-screen_width / 2 + 2, -screen_height / 2 + 2)
box.goto(-screen_width / 2 + 2, screen_height / 2 - 2)
box.penup()
screen.tracer(0)

scoreboard = Scoreboard()

# Create Alien
aliens = []
for j in range(4):
    for i in range(10):
        aliens.append( Alien(screen, j%2 + 1, i*50 - screen_width / 2 + 70 , j * 50) )

# Create Player
player = Player(screen)

screen.update()
screen.onkeypress(player.right, "Right")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.fire, "space")

game_over = False
while True and not game_over:
    player.bullet_move()

    # player bullet action :
    for bullet in player.bullet:
        for alien in aliens:
            if alien.distance(bullet) < 20 :
                alien.hide()
                bullet.hide()
                if alien.bullet is not None:
                    alien.bullet.hide()
                aliens.remove(alien)
                scoreboard.score += 1
                scoreboard.update_scoreboard("")

    if random.randint(1,10) == 5 and len(aliens) > 0:
        random.choice(aliens).fire()

    for alien in aliens:
        if alien.bullet is not None and alien.bullet.distance(player) < 20:
            game_over = True
            scoreboard.update_scoreboard("Game Over, You Lost ")
            break
        alien.bullet_move()

    if len(aliens) == 0:
        game_over = True
        scoreboard.update_scoreboard("You Won ")
        break
    else:
        MOST_RIGHT = 0
        MOST_LEFT = 0
        for alien in aliens:
            if MOST_RIGHT < alien.xcor():
                MOST_RIGHT = alien.xcor()
            if MOST_LEFT > alien.xcor():
                MOST_LEFT = alien.xcor()

        for alien in aliens:
            if MOST_RIGHT > screen_width/2 - 20:
                alien.ALIEN_FORWARD_DIRECTION = False
            elif MOST_LEFT < -screen_width/2 + 20:
                alien.ALIEN_FORWARD_DIRECTION = True
            alien.move()


    time.sleep(0.1)
    screen.update()

screen.exitonclick()