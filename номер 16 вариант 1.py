def f(n):
     if n <=1:
          return 1
     elif n == 2:
          return 2
     elif n > 2 and n % 3==0:
          return 2*n - f(n // 3)- f(n-1)
     else:
          return n+f(n-2)+f(n // 10)
count= 0
for  i in range(50, 101):
     F=f(i)
     if f(i)>50 and f(i)<=200:
          count+=1
print(count)