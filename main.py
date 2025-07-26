from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
screen = Screen()


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong:the famous arcade game")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
r_paddle.goto(350,0)
l_paddle.goto(-350,0)
ball = Ball()
score = Score()




screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down , "Down")
screen.onkey(l_paddle.up, "u")
screen.onkey(l_paddle.down , "d")



game_is_on = True
while game_is_on:
     time.sleep(0.1)
     screen.update()
     ball.move()
     if ball.ycor()>280 or ball.ycor()< -280:
          ball.y_move *= -1
     if ball.xcor() > 380:
          ball.goto(0,0)
          ball.x_move *= -1
          score.increase_left()
     if ball.xcor() < -380:
          ball.goto(0,0)
          ball.x_move *= -1
          score.increase_right()
     if ball.distance(r_paddle) < 50 and ball.xcor()>340:
          ball.x_move *= -1

     if ball.distance(l_paddle) < 50 and ball.xcor()<-340:
          ball.x_move *= -1




























screen.exitonclick()