import turtle as t
import time
from playsound import playsound
import keyboard


#Score variables
test=0
Ascore=0
Bscore=0

#Creating a window

win= t.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(800,600)
win.tracer(0)


#Creating Scorecard turtles
writerB= t.Turtle()
writerB.hideturtle()
writerA= t.Turtle()
writerA.hideturtle()

#Creating Start Menu
def start():
    starter = t.Turtle()
    starter.hideturtle()
    starter.pencolor("yellow")
    starter.penup()
    starter.goto(-170,200)
    starter.pendown()
    starter.write("۞ WELCOME TO PONG ۞",font=("Algerian", 18, "bold"))
    starter.penup()
    starter.goto(-130,0)
    starter.pendown()
    starter.write("Press Enter to play",font=("Algerian", 18, "normal"))
    starter.penup()
    starter.goto(-130,-50)
    starter.pendown()
    starter.write("Press Space to exit",font=("Algerian", 18, "normal"))
    starter.penup()
    starter.goto(-350,-200)
    starter.pendown()
    starter.write("Use WASD to control the left paddle. Use up and down arrow key to control the right.\nPrevent the ball from hitting the walls to earn a point. The first to reach 5 points will win. ",font=("Calibri", 14, "normal"))
    win.update()

    while test==0:
        if keyboard.is_pressed("space"):
            exit()
        elif keyboard.is_pressed("return"):
            playsound(r"C:\Users\RAHUL\Downloads\Welcome to game.wav")
            starter.clear()
            win.update()
            break

start()




#Creating left paddle

leftpaddle= t.Turtle()
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_len=1,stretch_wid=8)
leftpaddle.penup()
leftpaddle.goto(x=-350,y=0)
leftpaddle.showturtle()
win.update()

#Creating right paddle

rightpaddle= t.Turtle()
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_len=1,stretch_wid=8)
rightpaddle.penup()
rightpaddle.goto(x=350,y=0)
rightpaddle.showturtle()
win.update()


#Creating ball

ball= t.Turtle()
ball.shape("turtle")
ball.color("green")
ball.penup()
ball.setposition(-90,100)
ball.showturtle()
win.update()
ballx=0.4
bally=0.4

#Functions for movements of paddle
def leftdown():
    y= leftpaddle.ycor()
    y-=15
    leftpaddle.sety(y)
    win.update()

def leftup():
    y= leftpaddle.ycor()
    y+=15
    leftpaddle.sety(y)
    win.update()

def rightdown():
    y= rightpaddle.ycor()
    y+=15
    rightpaddle.sety(y)
    win.update()

def rightup():
    y= rightpaddle.ycor()
    y-=15
    rightpaddle.sety(y)
    win.update()

#Listeners
win.listen()
win.onkeypress(leftup,"w")
win.onkeypress(leftdown,"s")
win.onkeypress(rightdown,"Up")
win.onkeypress(rightup,"Down")
exit_game= False

while exit_game== False:
    win.update()
    ball.setx(ball.xcor()+ballx )
    ball.sety(ball.ycor()+bally )
    
    if ball.ycor() > 290:   # Right top paddle Border
        ball.sety(290)
        bally = bally * -1
        
    
    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        bally = bally * -1


    if ball.xcor() > 390:   # Right top paddle Border
        ball.setx(390)
        ballx = ballx * -1
        
    
    if ball.xcor() < -390:  # Left top paddle Border
        ball.setx(-390)
        ballx = ballx * -1

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        playsound(r"C:\Users\RAHUL\Downloads\4359__noisecollector__pongblipf4.wav")
        ball.setx(340)
        ballx = ballx * -1
        Bscore+=1
        writerB.clear()
        win.update()
        writerB.goto(90,270)
        writerB.pencolor("red")
        writerB.write(f"Ritul :{Bscore}",font=("Algerian", 18, "normal"))

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        playsound(r"C:\Users\RAHUL\Downloads\4359__noisecollector__pongblipf4.wav")
        ball.setx(-340)
        ballx = ballx * -1
        Ascore+=1        
        writerA.clear()
        win.update()
        writerA.goto(-250,270)
        writerA.pencolor("red")
        writerA.write(f"Rahul :{Ascore}",font=("Algerian", 18, "normal"))

    if Ascore==5:
        resultA= t.Turtle()
        resultA.hideturtle()
        resultA.pencolor("red")
        resultA.penup()
        resultA.goto(-170,0)
        resultA.pendown()
        resultA.write("Rahul has won!!!",font=("Algerian", 28, "normal"))
        playsound(r"C:\Users\RAHUL\Downloads\Game over.wav")
        break

    if Bscore==5:
        resultB= t.Turtle()
        resultB.hideturtle()
        resultB.pencolor("red")
        resultB.penup()
        resultB.goto(-170,0)
        resultB.pendown()
        resultB.write("Ritul has won!!!",font=("Algerian", 28, "normal"))
        playsound(r"C:\Users\RAHUL\Downloads\Game over.wav")
        break

time.sleep(2)
exit()
