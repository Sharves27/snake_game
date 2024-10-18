import turtle, time
from snake import *
from food import *
from scoreboard import * 


srn = turtle.Screen()
srn.setup(width=600, height=600)
srn.bgcolor('black')
srn.title("Snake_Game")
srn.tracer(0)
srn.listen()

# object creation
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# listening for the input from the keyboard
srn.onkey(fun=snake.up, key='Up')
srn.onkey(fun=snake.down, key='Down')
srn.onkey(fun=snake.right, key='Right')
srn.onkey(fun=snake.left, key='Left')


game_on = True
while game_on:
    snake.move()
    srn.update()
    time.sleep(0.1)


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_on = False
        snake.reset_snake()
        scoreboard.reset_scoreboard()


    for segment in snake.body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            # game_on = False
            snake.reset_snake()
            scoreboard.reset_scoreboard()


srn.mainloop()