loop = True
while loop:
    bacterias = int(input("How many B bacterias are there? "))
    time = int(input("How much time in minutes will we wait? "))

    if time % 2 == 0 :
        print(" After {0} minutes, we would have {1} bacterias".format(time,bacterias*time))
    else :
        print(" After {0} minutes, we would have {1} bacterias".format(time, bacterias*(time -1)))
    stop = input("Ban co muon dung chuong trinh? (Y/N)").upper()
    if stop == "Y" :
        break