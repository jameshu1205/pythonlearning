i = int(input('請輸入第一個數字:'))
j = int(input('請輸入第二個數字:'))
number = 0

if i > j:
    i, j = j, i

for x in range(1, i+1):

    if i % x == 0 and j % x == 0:
        number = x

if number != 1: 
    print("%d和%d的最大公因數為%d" % (i, j, number))

else:
    print("兩數互質")