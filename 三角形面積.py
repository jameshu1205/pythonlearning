a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a and b and c >= 0 and a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    print("面積為；", (s * (s - a) * (s - b) * (s - c)) ** 0.5)

else:
    print('不是三角形')