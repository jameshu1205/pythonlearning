number = int (input ("要生成幾個數:"))
x = 1
y = 1

if number <= 0:
    print('錯誤')

elif number == 1:
    print('*')

elif number == 2:
    print('*')
    print('*')

else:
    print('*')
    print('*')

    for i in range (0, number - 2):
        z = x + y

        for j in range (0, z):
            print('*',end ='')
        
        print('')

        x = y
        y = z