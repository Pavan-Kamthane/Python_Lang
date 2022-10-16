'''Program to demonstrate event driven programming'''
import turtle
turtle.setup(500,500)
wn = turtle.Screen()
wn.title("Multi mouse clicks!")
wn.bgcolor("yellow")
goku = turtle.Turtle()
goku.color("orange")
goku.shape("turtle")
goku.pensize(4)
vegeta = turtle.Turtle()
vegeta.color("blue")
vegeta.shape("turtle")
vegeta.forward(100)
def handler_for_goku(x, y):
    wn.title("goku clicked at {0}, {1}".format(x, y))
    goku.left(45)
    goku.forward(75)
def handler_for_vegeta(x, y):
    wn.title("vegeta clicked at {0}, {1}".format(x, y))
    vegeta.right(60)
    vegeta.forward(60)

#On mouse click the turtle associated with this object would move
goku.onclick(handler_for_goku)          
vegeta.onclick(handler_for_vegeta)
wn.mainloop()

'''Code provided by Akshaj Vishwanathan'''
