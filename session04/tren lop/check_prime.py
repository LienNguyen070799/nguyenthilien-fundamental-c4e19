loop = True
i = 2
numb = int(input(" moi nhap vao so bat ki: "))
while i <= (numb** 0.5):
    
    if numb % i == 0 :
        loop = False
        break
    i+= 1
if loop :
    print("{0} is a prime number".format(numb))

else:
    print(numb, "khong la so nguyen to")
       