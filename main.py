import turtle
import pandas as n
read = n.read_csv("50_states.csv")
states = list(read["state"])
position_x = list(read["x"])
position_y = list(read["y"])
turtle1 = turtle.Turtle()
screen = turtle.Screen()
screen.title("us state game")
img = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle1.shape("blank_states_img.gif")
true = True
while true:


    screen1 = screen.textinput("guess the state", "write the ans here")
    if screen1 == "exit":
        true = False
    for i in range(0,50):
        if screen1 == states[i]:
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(position_x[i],position_y[i])
            turtle.write(screen1)

def khesari(x,y):
    print(x,y)

turtle.onscreenclick(khesari)
turtle.mainloop()