from turtle import Screen,Turtle
from snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(height  = 600,width = 600)

screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
#Animating the snake's segments
score = scoreboard.high_score

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Controlling a snake's movements

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")


    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        scoreboard.update_score()
        snake.add_turtle()
        food.move()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        if scoreboard.high_score > score:
            score = scoreboard.high_score
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.

    for turtle in snake.all_turtles[1:]:

        if snake.head.distance(turtle) < 10:
            if scoreboard.high_score > score:
                score = scoreboard.high_score
            scoreboard.reset()
            snake.reset()

    #if head collides with any segment in the tail:
        #trigger game over




screen.exitonclick()
