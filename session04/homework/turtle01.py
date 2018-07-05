from turtle import *
shape("turtle")
color("green")
speed(-1)
n =int(input(" nhap vao so bat ki: "))
for i in range(n):
    for j in range(4):
        forward(100)
        left(90)
    left(360/n)
mainloop()

