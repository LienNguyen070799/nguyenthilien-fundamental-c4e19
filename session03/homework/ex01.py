clothes = [" T-shirt", "Sweater"]
loop = True
while loop:
    choose = input( "Welcome to our shop. What do you want (C,R,U,D) ?")
    
    if choose == "R" or choose == "r" :
        print (" Our items: ", end= "")
        print (*clothes, sep =", ")
       
    elif choose == "C" or choose == "c" :
        new_item = input (" Enter new item: ")
        clothes.append(new_item)
        print(" Our items: ", end= "")
        print(*clothes, sep =", ")
       
    elif choose == "U" or choose == "u" :
        update = int(input(" update position: "))
        if update > len(clothes):
            print("invalid update location! Try again!")
        else:
            change = input (" New item: ")
            clothes [update - 1] = change
            print(" Our items: ", end ="")
            print(*clothes, sep =", ")
    elif choose == "D" or choose == "d" :
        pos_del = int(input(" Delete position: "))
        if pos_del > len(clothes):
            print("invalid update location! Try again!")
        else:
            del(clothes[pos_del - 1])
            print( " Our items: ", end = "")
            print(*clothes, sep = ",")
    elif choose == "Exit" or choose == "exit" or choose == "EXIT" :
        print("Thank you! See you again!^-^")
        break
    else :
        print( "Sorry, try again! ")


