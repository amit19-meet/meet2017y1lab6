import turtle #python needs this to use all the turtle functions
#turtle.shape("turtle") #changes the shape to a turtle
#square = turtle.clone() #creates new turtle and saves it in square
#square.shape("square") # changes the shape of the second turtle to a square
#square.goto(100, 100) # moves square to ( x= 100, y= 100)
#square.goto(100,0)
#square.goto(100,100)
#square.goto(0,100)
#square.goto(0,0)
#triangle = turtle.clone() #creates new turtle and saves it in triangle
#triangle.shape("triangle") #changes the shape of the third turtle to a triangle
#triangle.goto(100,0)
#triangle.goto(50,25)
#triangle.goto(0,0)
#square.penup()
#square.goto(200,200)
#square.stamp()
#square.goto(100,50)
#triangle.penup()
#triangle.goto(200,200)
#triangle.stamp()
#triangle.goto(100,50)
UP_ARROW = "Up" #these are the codes that correspond to the keys
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP

def up():
    global direction
    print("you pressed Up!")

def down():
    global direction
    direction = DOWN
    print("you pressed Down!")

def left():
    global direction
    direction = LEFT
    print("you pressed Left!")

def right():
    global direction
    direction = RIGHT
    print("you pressed Right!")

#these lines of code calls the right functions when you press keys
turtle.onkeypress(up, UP_ARROW) #move up when you press up
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

    



turtle.mainloop() #makes this the last line in ypur turtle code
