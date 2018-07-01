from turtle import *
speed(-1)
colors = ["red","blue","brown","yellow","grey"]
n = 3
for i in range (5):
    for j in range (n): 
        color (colors[i])
        forward (100)
        left(360/n)
    n += 1
mainloop()


