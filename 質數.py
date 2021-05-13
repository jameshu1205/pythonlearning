from math import sqrt

number = int(input("請輸入一個正整數："))
final = int(sqrt(number))
in_prime = 1

for i in range(2, final + 1):

    if number % i == 0:
        in_prime = 0
        break

if in_prime and number != 1:
    print(number, '是質數')

else:
    print(number, "不是質數")