

number= int(input(" nhap so bat ki : "))
original_number = number
n = True
count = 0
while number > 0:
    number = number//10
    

       
    count += 1

print("{0} has {1} digits".format(original_number, count))