print("Guess your number game\nNow thank or a number (0-100) then press Enter")
input()
print("""
All have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 's'maller than your guess
'l' if my guess is 'l'arger than your guess
""")
low = 0
high = 101
loop = True
while loop:
    mid = (low + high)//2
    nhap = input("Is {0} your number?".format(mid)).lower()
    if  nhap == "c":
        print(" I knew it! ")
        break
    elif nhap == "l":
        high = mid
        
        # if mid == low or mid == high:
        #     break
    elif nhap == "s":
        low = mid
       
        # if mid == low or mid == high:
        #     break
    


    
    

