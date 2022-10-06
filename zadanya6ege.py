import turtle 
from turtle import *

count = 0 # объявляем переменную для подсчета выполненных циклов
left(90) #Поворачиваем черепшку на 90 градусов
while count<7: #повтор 7 раз
    forward(100) #вперед 10 раз
    right(120) #из условия на 120 градусов
    count+=1
done()
    