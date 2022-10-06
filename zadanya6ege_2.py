import math

count=0 #объявляем переменную для подсчета точек
for x in range(11): #перебираем х
    for y in range(11): #перебираем y
        if x>0 and x*math.sqrt(3)/3<y<(10+-1*math.sqrt(3)/3*x):
            count+=1
print(count)
    