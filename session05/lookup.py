word = {"nc":"noi chuyen", "ng": "nguoi", "vk" : "vo", "ck": "chong"}
while True:
    for key in word.keys():
        print(key, end = "\t")
    print()

    code = input("Your code? ")
    if code in word:
        print(word[code])

    else: 
        nhap= input(" tu nay ko co trong tu dien, ban co muon them khong?(Y/N) ").upper()
        if nhap == "Y" :
        
            them = input("them tu vao : ")
            nghia = input("them nghia cua tu :")
            word[them] = nghia
            print(word)
        else: 
            print(" Bye")
            break
        
