long = int (input('請輸入高:'))
i = 0

while (i < long):
    j = 0

    while (j < i):
        print ('*', end = " ")
        j += 1

    while (j == i):
        print ('*')
        j += 1
    
    i += 1    