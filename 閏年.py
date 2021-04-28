year = int (input ('請輸入年份：'))

if (year < 0):
    print ('錯誤')
    quit()

elif (year % 4 != 0):
    i = False

elif (year % 4 == 0 and year % 100 != 0):
    i = True

elif (year % 100 == 0 and year % 400 != 0):
    i = False

else:
    i = True

if (i == True):
    print ('是閏年')

else:
    print ("不是閏年") 