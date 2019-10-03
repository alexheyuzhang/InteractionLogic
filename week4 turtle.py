
from turtle import * 
import random

window = Screen()
window.bgcolor('#fcb1b1')
colors = ['#b22b2b', '#ef3f3f', '#dd9494', '#f7b5b5','#c11010','#ba1717','#7a2929','#fc1717','ff5050']
pensize(3)


speed(0)
pencolor('#6b0101')


def draw_shape():
    fillcolor(colors[random.randint(0,len(colors)-1)])
    begin_fill()
    forward(15)
    left(50)
    forward(15)
    left(130)
    forward(15)
    left(50)
    forward(15)
    end_fill()
    fillcolor(colors[random.randint(0,len(colors)-1)])
    left(40)
    forward(15)
    left(90)
    forward(15)
    begin_fill()
    left(50)
    forward(15)
    left(40)
    forward(15)
    left(140)
    forward(15)
    left(40)
    forward(15)
    left(90)
    end_fill()
    setheading(heading()+10)

for i in range(37):
  draw_shape()

penup()
goto(random.randint(-50,50))
pendown()

for c in range (50):

  for b in range(37):
    draw_shape()

  penup()
  goto(random.randint(-10,100))
  pendown()




    
