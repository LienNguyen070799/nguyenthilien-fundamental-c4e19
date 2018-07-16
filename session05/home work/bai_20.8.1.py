sentence = input(" Moi nhap vao day string bat ky : ").lower()
words = list(sentence)
words.sort()
words_2 = []
loop = True
for i in range(len(words)) :
    if words[i] == " ":
        loop = True
    else:
        words_2.append(words[i])
count_words = {}
for w in words_2:
    count_words [w] = count_words.get(w,0) + 1
for a ,b in count_words.items() :
    print("{0} : {1} times".format(a,b))
