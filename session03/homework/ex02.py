sizes = [5,7,300,90,24,50,75]
print ("Hello, My name is Lien and these are my ship sizes: ")
print (*sizes, sep =", ")
print("Now my biggist sheep has size", max(sizes), "let's shear it!")
sizes[sizes.index(max(sizes))] = 8
print("After shearing, here is my flock: ")
print(*sizes, sep =", ")
for i in range(7):
    sizes[i] += 50
print("My ship sizes in the following month: ")
print(*sizes, sep =", ")