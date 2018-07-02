clothes = [" T-shirt", "Sweater"]
loop = True
while loop:
    choose = input( "Welcome to our shop. What do you want (C,R,U,D) ?")
    
    if choose == "R" :
        print (" Our items: ", end= "")
        print (*clothes, sep =", ")
       
    elif choose == "C" :
        new_item = input (" Enter new item: ")
        clothes.append(new_item)
        print(" Our items: ", end= "")
        print(*clothes, sep =", ")
       
    elif choose == "U" :
        update = int(input(" update position: "))
        if update > len(clothes):
            print("invalid update location! Try again!")
        else:
            change = input (" New item: ")
            clothes [update - 1] = change
            print(" Our items: ", end ="")
            print(*clothes, sep =", ")
    elif choose == "D":
        pos_del = int(input(" Delete position: "))
        if pos_del > len(clothes):
            print("invalid update location! Try again!")
        else:
            del(clothes[pos_del - 1])
            print( " Our items: ", end = "")
            print(*clothes, sep = ",")
    elif choose == "Exit":
        print("Thank you! See you again!^-^")
        break
    else :
        print( "Sorry, try again! ")


