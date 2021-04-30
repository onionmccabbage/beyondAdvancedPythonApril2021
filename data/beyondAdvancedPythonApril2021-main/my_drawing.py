import turtle # pip install turtle

turtle.setup(500, 500)
window = turtle.Screen()
window.title('rotate and draw using the arrow keys')
window.bgcolor('lightblue')
Gordon = turtle.Turtle()

def moveForward():
    Gordon.forward(50)

def turnLeft():
    Gordon.left(30)

def turnRight():
    Gordon.right(30)

def start():
    window.onkey(moveForward, 'Up')
    window.onkey(turnLeft, 'Left')
    window.onkey(turnRight, 'Right')
    # start listening for events
    window.listen()
    # we need a run loop!
    window.mainloop()

if __name__ == '__main__':
    start()