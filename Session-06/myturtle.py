import turtle

smart = turtle.Turtle()
#Loop 4 times. Everything I want to repeat is intended

for i in range(4) :
    smart.forward(50)
    smart.right(90)

#This isnt' intended, so we arent repeating it
turtle.done()