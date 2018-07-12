# nếu số tháng lớn hơn bằng 2 thì số thỏ tháng sau = số thỏ tháng trước + số thỏ tháng trước nữa
rabbit = int(input(" Mời nhập vào số cặp thỏ ban đầu : "))
month = int(input(" Thời gian nuôi thỏ : "))
print("Month 0 has {0} pair(s) of rabbit".format(rabbit))
rabbit_1 = rabbit
for i in range(1,month+1) :
    rabbit,rabbit_1 = rabbit_1, rabbit + rabbit_1
    print("Month {0} has {1} pair(s) of rabbit".format(i,rabbit_1))


