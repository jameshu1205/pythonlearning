import math

r = float (input ('請輸入半徑：'))
l = float (2 * r * math.pi)
a = float (r * r * math.pi)

print ('圓周長：%1f,園面積：%1f'%(l,a))