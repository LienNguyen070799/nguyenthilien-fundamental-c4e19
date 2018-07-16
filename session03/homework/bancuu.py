sizes = [5,7,300,90,24,50,75]

print("Hello, My name is Lien and here is my flock: ")
print(*sizes, sep =", ")
print("Now my biggest sheep has size ",max(sizes),"let's shear it!")
sizes[sizes.index(max(sizes))] = 8
print("After shearing, here is my flock: ")
print(*sizes,sep =", ")

for i in range (3):
    for j in range (7):
        
        sizes [j] += 50
    print("MONTH", i+1)
    print("One month has passed,now here is my flock: ")
    print(*sizes,sep =", ")
    if i<2:
        print("Now my biggest sheep has size",max(sizes),"let's shear it!")
        sizes[sizes.index(max(sizes))] = 8
        print("After shearing, here is my flock: ")
        print(*sizes,sep =", ")
total = sum(sizes)
print("My flock has size in total: ",total)
print("I would get",total,"*",2,"$ =", total*2,"$")






















