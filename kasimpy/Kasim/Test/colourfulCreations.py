from turtle import *

screen = Screen()
screen.setup(400, 400)
screen.bgcolor('#6699ff')

colours = {
    'myLime': '#ccff99',
    'myAqua': '#66ffcc',
    'myPeach': '#ffcc99'
    } 

penup()
goto(0,100)

color(colours['myPeach'])
style = ('Times', 50, 'bold')
write('HELLO', font=style, align='center' )

right(90)
forward(60)
color(colours['myLime'])
write('1000', font=style, align='center' )

right(10)
forward(60)
circle(50)
dot(100)
hideturtle()
