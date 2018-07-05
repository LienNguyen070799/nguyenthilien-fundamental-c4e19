from turtle import *
color("yellow")
speed(-1)
n =int(input(" nhap vao so bat ki : "))
for i in range (0,n,2) :
    for j in range (4) :
        forward(10+i)
        left(90)
    left(10)
mainloop()