import turtle

###they didn't work so I used pygame
#from playsound import playsound
#import winsound
#winsound.PlaySound("retro.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

#just for music
import pygame 
pygame.init()
music=pygame.mixer.music.load("retro.wave")
pygame.mixer.music.play(-1)

# initializing screen, its coordinates is like normal maths
wind = turtle.Screen()
wind.title("Ping Pong")  # screen title
wind.bgcolor("black")  # Background color
wind.setup(width=800, height=600)
wind.tracer(0)  # Stops the window from updating automatically

# Player1
Player1 = turtle.Turtle()  # initializes turtle object
Player1.speed(0)  # set the speed of the animation
Player1.shape("square")
Player1.color("yellow", "blue")
Player1.shapesize(stretch_wid=5, stretch_len=1)
Player1.penup()  # prevents the object from drawing lines
Player1.goto(-350, 0)  # determine the position of the object

# Player2
Player2 = turtle.Turtle()
Player2.speed(0)
Player2.shape("square")
Player2.color("yellow", "red")
Player2.shapesize(stretch_wid=5, stretch_len=1)
Player2.penup()
Player2.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("pink", "white")
Ball.shapesize(stretch_wid=1, stretch_len=1)
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.2  # this number depends on your device
Ball.dy = 0.2

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center",
            font=("Courier", 24, "normal"))


# Functions

def Player1_up():
    y = Player1.ycor()
    y += 20
    Player1.sety(y)


def Player1_down():
    y = Player1.ycor()
    y -= 20
    Player1.sety(y)


def Player2_up():
    y = Player2.ycor()
    y += 20
    Player2.sety(y)


def Player2_down():
    y = Player2.ycor()
    y -= 20
    Player2.sety(y)


# Key Binding
wind.listen()
wind.onkeypress(Player1_up, "w")
wind.onkeypress(Player1_down, "s")
wind.onkeypress(Player2_up, "Up")
wind.onkeypress(Player2_down, "Down")


# main game loop
while True:
    wind.update()  # update the screen every time the loop run

    # moving the Ball
    # Ball starts at 0 and everytime the loop runs--->+0.5 on x axis
    Ball.setx(Ball.xcor()+Ball.dx)
    # Ball starts at 0 and everytime the loop runs--->+0.5 on y axis
    Ball.sety(Ball.ycor()+Ball.dy)

    # Border check
    if Ball.ycor() > 290:  # if ball is at top border
        Ball.sety(290)  # set y coordinate +290
        Ball.dy *= -1  # reverse direction

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:  # if ball is at right border
        Ball.goto(0, 0)  # return ball to center
        Ball.dx *= -1  # reverse direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2),
                    align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2),
                    align="center", font=("Courier", 24, "normal"))

    # Collision between the Ball and Player2
    if(Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Player2.ycor()+40 and Ball.ycor() > Player2.ycor()-40):
        Ball.setx(340)
        Ball.dx *= -1


    # Collision between the Ball and Player1
    if(Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Player1.ycor()+40 and Ball.ycor() > Player1.ycor()-40):
        Ball.setx(-340)
        Ball.dx *= -1
