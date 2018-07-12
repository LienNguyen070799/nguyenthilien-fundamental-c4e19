numbers = [1,3,5,7,2,3,7,9,5,3,3,5]
a = int(input(" Moi nhap so bat ki co trong list : "))
# 1
if a in numbers: 
    print("{0} appears {1} times in my list".format(a,numbers.count(a)))
else :
    print( " so {0} khong co trong list".format(a))
# 2
count = 0
for i in numbers:
    if i == a:
        count +=1
print("{0} appears {1} times in my list".format(a,count))

    