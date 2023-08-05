import turtle

#Window creation
gWindow = turtle.Screen()
gWindow.title("Pong from scratch")
gWindow.bgcolor("black")
gWindow.setup(width=800, height=600)
gWindow.tracer(0)

#Player 1's paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(5, 1)
paddle_1.penup()
paddle_1.goto(-350, 0)

#Player 2's paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(5, 1)
paddle_2.penup()
paddle_2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = 0.09

#Scoring System Definition
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align = "center", font=("Courier", 24, "normal"))
score_1 = 0
score_2 = 0

#Move Paddle 1
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

#Move Paddle 2
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#Keybinds
gWindow.listen()
gWindow.onkeypress(paddle_1_up, "w")
gWindow.onkeypress(paddle_1_down, "s")
gWindow.onkeypress(paddle_2_up, "Up")
gWindow.onkeypress(paddle_2_down, "Down")

#Window updation (Main game loop)
while True:
    gWindow.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Screen boundaries
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
    
    if(ball.xcor() > 390):
        ball.goto(0,0)
        ball.dx = -0.09
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align = "center", font=("Courier", 24, "normal"))

    if(ball.xcor() < -390):
        ball.goto(0,0)
        ball.dx = 0.09
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align = "center", font=("Courier", 24, "normal"))

    #Collision control
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1.03

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1.03