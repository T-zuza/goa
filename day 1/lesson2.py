from turtle import *


#we want to paint a house
speed(20)
#step 1 draw a scuare
width(3)
color("blue")
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square
#drawing a door
forward(70)
color ("green")
begin_fill()


left(90)
forward(120)    #haight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()






penup()
goto(200, 200)
pendown()


#drowing a roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing right window
left(90)
color ("blue")

penup()
goto(200, 200)
pendown()
right(60)
forward(200)
right(90)
forward(70)
left(90)
right(90)
right(90)
color("green")
forward(120)
right(90)
color("yellow")
forward(40)
right(90)
forward(40)
right(90)
forward(40)
begin_fill()
color("yellow")

#left window

color("yellow")
begin_fill()
color ("green")
forward(60)
color("yellow")
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()









exitonclick()
