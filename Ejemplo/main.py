import turtle
print("Hello World")

tortuga = turtle.Turtle()

tortuga.left(45)
tortuga.forward(50)
tortuga.right(90)
tortuga.forward(50)
tortuga.right(135)
tortuga.forward(75)
for i in range(4):
    tortuga.forward(50)
    tortuga.right(90)

turtle.done()