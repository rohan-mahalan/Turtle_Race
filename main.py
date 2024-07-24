from turtle import Screen
from others import OTHERS
from finish_line import FINISH
import time


guess = input("Place your bet\n1.Red\n2.Orange\n3.Blue\n4.Violet\n5.Black\n").lower()
winner = ""

y = Screen()
line = FINISH()
y.tracer(0)
rivals = OTHERS()
y.update()

y.screensize(canvwidth=500, canvheight=500)
y.title("Turtle Race")
flag = 1

while flag == 1:
    time.sleep(0.5)

    rivals.movement()
    y.update()
    for i in rivals.segments:
        if i.xcor() > 310:
            winner = i.color()
            flag = 0

if guess == winner:
    print("You Won!!!")
else:
    print(f"You Lost. The winner is {winner[0].capitalize()}")

y.exitonclick()
