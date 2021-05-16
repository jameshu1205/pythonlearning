number = int (input ("要生成幾個數:"))
x = 1
y = 1

if number <= 0:
    print('錯誤')

elif number == 1:
    print(x)

elif number == 2:
    print(x)
    print(y)

else:
    print(x)
    print(y)

    for i in range (0, number - 2):
        z = x + y

        print(z)

        x = y
        y = z