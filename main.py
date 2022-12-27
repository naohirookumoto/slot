import my_module
import turtle_control
import keyboard
import turtle

my_module.getPosition()
speed = 5
speed_rgn = 10

while True:
    if keyboard.is_pressed("w"):
        turtle_control.forward(speed)
    if keyboard.is_pressed("s"):
        turtle_control.backward(speed)
    if keyboard.is_pressed("d"):
        turtle_control.right(speed_rgn)
    if keyboard.is_pressed("a"):
        turtle_control.left(speed_rgn)
    if keyboard.is_pressed("h"):
        turtle_control.home()
    if keyboard.is_pressed("q"):
        print("\n終了します")
        break