import turtle
import time

wn = turtle.Screen()
wn.setup(width=450, height=450)
wn.bgcolor("red")
wn.title("Analog Clock Application")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)


def draw(saat, minute, second, pencil):
    pencil.begin_fill()
    pencil.color("black")
    pencil.up()
    pencil.goto(0, 210)
    pencil.setheading(180)
    pencil.color("black")
    pencil.pendown()
    pencil.circle(210)
    pencil.end_fill()

    pencil.up()
    pencil.goto(0, 0)
    pencil.setheading(90)
    pencil.begin_fill()
    pencil.color("white")
    for i in range(12):
        pencil.forward(190)
        pencil.pendown()
        pencil.fd(20)
        pencil.penup()
        pencil.goto(0, 0)
        pencil.right(30)

    pencil.end_fill()
    # hour
    pencil.up()
    pencil.goto(0, 0)
    pencil.color("blue")
    pencil.setheading(90)
    info = (saat / 12) * 360
    pencil.rt(info)
    pencil.pendown()
    pencil.forward(100)

    # minute
    pencil.up()
    pencil.goto(0, 0)
    pencil.color("gold")
    pencil.setheading(90)
    info = (minute / 60) * 360
    pencil.rt(info)
    pencil.pendown()
    pencil.forward(80)

    # second
    pencil.up()
    pencil.goto(0, 0)
    pencil.color("hotpink")
    pencil.setheading(90)
    info = (second / 60) * 360
    pencil.rt(info)
    pencil.pendown()
    pencil.forward(50)


while True:
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    draw(hour, minute, second, pen)
    wn.update()
    pen.clear()
