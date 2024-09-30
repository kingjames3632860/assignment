from turtle import *

def drawman():
    setup(800,800)
    speed(3)
    bgcolor("white")
    penup()
    goto(-150,150)
    pendown()
    circle(30)
    penup()
    goto(-150,150)
    setheading(-90)
    pendown()
    fd(100)
    penup()
    goto(-150,100)
    setheading(-30)
    pendown()
    fd(75)

    penup()
    goto(-150,100)
    setheading(-120)
    pendown()
    fd(75)
     
    penup()
    goto(-150,50)
    setheading(-120)
    pendown()
    fd(100)
    
    penup()
    goto(-150,50)
    setheading(-60)
    pendown()
    fd(100)
    
    
    penup()
    goto(-85.5,62.5)
    pendown()
    fillcolor("yellow")
    begin_fill()
    circle(10)
    end_fill()
    penup()
    goto(-187,37.0)
    setheading(-150)
    pendown()
    fd(75)
    penup()
    goto(-272.5,7)
    pendown()
    fillcolor("green")
    begin_fill()
    circle(30)
    end_fill()
    hideturtle()
    exitonclick()

drawman()
