favor=["a","b","c"]
for index,item in enumerate(favor):
    print(index+1, item, sep = ". ")
print("* "*20)
pos = int(input("vi tri muon update: "))
change = input("update di: ")
favor[pos-1] = change
print(*favor)
# remove del pop
