word1 = "champion"
words = list(word1)
print(words)
words2 = []
# for i in range (8):
while len(words) >0 :
    import random
    rand = random.choice(words)

    words.remove(rand)
    
    
    words2.append(rand)
print(*words2, sep ="  ")
nhap = input ("your answer: ")
if nhap == word1:
    print("hura")
else:
    print(":(")
