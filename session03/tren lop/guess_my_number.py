from random import *

r= randint(1,100)
print("so ngau nhien ", r )


n= True 
count= 0
while n:
    guess = int(input(" so : "))
    if r ==guess:
        print ("bingo")
    elif r> guess:
        print(" too small")
    else:
        print("large")
        break
    count+=1
    if count==7:
        print(" you lose")
        n= False
