from turtle import *

#i want to draw a house
speed(10)
width(3)
color ("blue")


forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)

#end of scuare

penup()
goto (0, 0)
pendown()

#drawing window and door
width(3)
color("blue")

color("blue")
begin_fill()

left(90)
forward(110)
width(5)
color("green")
left(90)
forward(180)   #haight of the door
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
right(90)
forward(150)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
left(180)
forward(180)
penup()
goto (300, 300)
pendown()

#drawing roof
color("red")
begin_fill()

left(90)
forward(40)
left(90)
forward(50)
left(45)
forward(60)
left(45)
forward(300)
left(45)
forward(60)
left(45)
forward(50)
left(90)
forward(390)

end_fill()

#end drawin roof

color("red")

begin_fill()


















exitonclick()
