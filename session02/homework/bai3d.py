# i:
for i in range(9):
    if i%2==0 :
        for j in range(9):
            if j%2==1:
                print(0,end="  ")
            else:
                print(1,end= "  ")
    else:
        for j in range (9):
            if j%2==0:
                print(0,end="  ")
            else:
                print(1,end="  ")
    print()



# ii:
n=int(input("so bat ki: "))
for i in range(n):
    if i%2==0 :
        for j in range(n):
            if j%2==1:
                print(0,end="  ")
            else:
                print(1,end= "  ")
    else:
        for j in range (n):
            if j%2==0:
                print(0,end="  ")
            else:
                print(1,end="  ")
    print()
        
