import math
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self,a):
        self.a = a
    def get_area_circle(self):
        return self.a ** 2 * math.pi


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def getWidth(self):
#         return  self.width
#
#     def getWidth(self):
#         return self.height
#
#     def getArea(self):
#         return self.width * self.height
#

# name = input('Введите ваше имя ')
# age = input('Введите ваш возраст ')
# print(name, age)

# num = int(input('Введите число '))
# if num % 2 == 0:
#     print('Четное')
# else:
#_______________________________________________________________
# #Сортировка при вводе 0, выход из цикла и формирования списка.
# num = int(input('Введите целое число '))         #4
# data = []
# while num != 0:                                  # data = [4, 5 ...]
#     data.append(num)
#     num = int(input('Введите целое число '))     # 5
# # data.sort()
# print(data)
# #_____________________________________________________________
##______________________________________________________________
# data = [2, 3, 4]
# data.append(5)
# print(data)
##______________________________________________________________
# s = 0
# x = int(input())
# while x > 0:
#     binDigit = x % 2
#     s += binDigit
#     x //= 2
# print(s)

# for x in range:
#     print(x ** 2)
# n = int(input())
# s = 0
# for x in range(1, n + 1):
#     s += x ** 2
# print(s)
# N = int(input())
# factorial = 1
# for x in range(1, N + 1):
#     factorial *= x
# print(factorial)

# s = 0
# d = 1
# a = int(input())
# n = int(input())
# for i in range(0, n + 1):
#     s += d
#     d *= a
# print(s)

# x = int(input())
# for delitel in range(1, x + 1):
#     if x % delitel == 0:
#         print(delitel, end = ' ')
#def имя_функции(аргументы):
#   инструкции
#   return - список_выражений   None
# имя_функции()

# def great(name):
#     print('привет ' + name + '. Доброе утро!')
# great('Джон')

#возвращаемое значение - return

# def absolute_value(num):
#     if num >= 0:
#         return  num
#     else:
#         return -num
# print(absolute_value(2))
# print(absolute_value(-4))

# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)
#
# total = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
# print('Сумма чисел больших 10 равна', total)

# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

# total = 0
# for i in range(10):
#     num = int(input())
#     total = total + num
# average = total / 10
# print('Среднее значение равно', average)

# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# largest = int(input())
# for i in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# smallest = int(input())
# for i in range(9):
#     num = int(input())
#     if num < smallest:
#         smallest = num
# print('Наименьшее число равно', smallest)

# total = 0
# print('старт цикла for')
# for i in range(1, 6):
#     print(f'{i} круг: total = {total}   i = {i}, total + i = {total + i}')
#     total += i
# print(total)

# myfile = open('hello.txt', 'r')
# file = myfile.read()
# print(file)
# myfile.close()

# newfile = open('test.txt', 'w', encoding="utf8")
# newfile.write('tttt')
# print('zzzz', file=newfile)
# newfile.close()

# total = 0
# n = int(input())
# for i in range(n):
#     num = int(input())
#     total +=num
# print(total)

# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
# events = [
#     {
#         "timestamp": 1554583508000,
#         "type": "itemViewEvent",
#         "session_id": "O:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#         "timestamp": 1555296337000,
#         "type": "itemViewEvent",
#         "session_id": "O:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#         "timestamp": 1549461608000,
#         "type": "itemViewEvent",
#         "session_id": "O:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     }
# ]
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
#                       event_type=event.get("type"),
#                       session_id=event.get("session_id"))
#     print(event_obj.timestamp)

#import datetime

# class Product:
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available_set(self):
#         return True if self.quantity_in_stock > 1 else False
#
#
# eggs = Product("eggs", "food", 5)
#
# print(eggs.is_available())