choose = int (input ('請選擇要輸入的三角形:\n1. 直角三角形(靠左)\n2. 直角三角形(靠右)\n3. 倒直角三角形'))
long = int (input ('要輸出多高的三角形:'))

if (choose == 1):

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

elif (choose == 2):

    i = 0

    while (i < long):

        j = 0

        while (j < long - i):
            print (' ',end =' ')
            j += 1

        while (long - i <= j < long):
            print ('*',end = ' ')
            j += 1

        while (j == long):
            print ('*')
            j += 1
        
        i += 1

elif (choose == 3):

    i = 0

    while (long >= i):

        j = 0

        while (j < long - 1):
            print ('*', end = ' ')
            j += 1

        while (j == long - 1):
            print ('*')
            j += 1

        long -= 1
            