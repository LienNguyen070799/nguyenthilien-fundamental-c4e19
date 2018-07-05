
# cach 1
bal = int(input("Enter your balance : "))
print(" Your updated balance : ${:0,d}".format(bal))
# cach 2
bal = int(input("Enter your balance : "))
import locale 
locale.setlocale(locale.LC_ALL, "en_US")
tien = locale.currency(bal,grouping = True)
print("Your updated balance : ",tien)

