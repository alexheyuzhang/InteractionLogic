
from turtle import * 
import random

colors = ['#b22b2b', '#ef3f3f']
#fillcolor('purple')
pensize(3)
pencolor('#6b0101')
speed(0)




def draw_shape():
    fillcolor(colors[0])
    begin_fill()
    forward(20)
    left(50)
    forward(20)
    left(130)
    forward(20)
    left(50)
    forward(20)
    end_fill()
    fillcolor(colors[1])
    left(40)
    forward(20)
    left(90)
    forward(20)
    begin_fill()
    left(50)
    forward(20)
    left(40)
    forward(20)
    left(140)
    forward(20)
    left(40)
    forward(20)
    left(90)
    end_fill()
    setheading(heading()+10)

for i in range(38):
  draw_shape()


penup()
goto(random.randint(-50,50))
pendown()

for b in range(38):
  draw_shape()
  



    
