name = input ("Your full name : ")
name2 = name.title()
word = name2.split(" ",len(name2))

word2=[]
for index,item in enumerate(word) :

    if word[index] == '' :
        word = word
       
    else:
        word2.append(item)

print("Updated : ",*word2)