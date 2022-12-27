import turtle

kame = turtle.Turtle()
kame.shape('turtle')
kame.speed(10)

def forward(speed):
    kame.forward(speed)

def backward(speed):
    kame.backward(speed)

def right(speed):
    kame.right(speed)

def left(speed):
    kame.left(speed)

def home():
    kame.penup()
    kame.home()
    kame.pendown()
