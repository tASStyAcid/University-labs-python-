#1)	Напишите программу, которая будет выводить все нечетные числа из диапазона от 39 до
#248 и остановится, если встретится 139.
print('Задача №1') 
y = [i for i in range(39, 248)]
x = []
print(y)
n = len(y)
i = 0
while i < n:
    if y[i] != 139:
        if y[i] % 2 == 1:
            x.append(y[i])
        i += 1
    else:
        break
print(x)     
print('\n')   

#2)	Дан список list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]. 
#Необходимо вывести элементы, которые одновременно  меньше 30 и  делятся на 3 без остатка. Все остальные элементы списка необходимо просуммировать и вывести конечный результат.
print('Задача №2') 
list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
el = []
n = len(list)
sum = 0
j = 0
while j < n:
    if list[j] < 30 and list[j] % 3 == 0:
        el.append(list[j])
    else:
        sum += list[j]
    j += 1
print(el, '\n', sum)
print('\n')

#3)	Напишите программу, которая будет по номеру месяца выводить время года. 
#Например, если введено 2, то следует вывести «Зима».
print('Задача №3') 
month = int(input()) % 12
if month < 3 or month == 12:
    print('Winter')
elif month < 6:
    print('Spring')
elif month < 9:
    print('Summer')
elif month < 12:
    print('Autumn')
print('\n')
    
#4)	Выведите все числа от 0 до N, где 

#a.	N=66
#b.	N= –31

print('Задача №4') 
p = []
N = int(input())
k = 0
while k < N + 1 and N > 0:
    p.append(k)
    k += 1
else:
    k = N
    while k < 0:
        p.append(k)
        k += 1
print(p, '\n')

#5)	Вывести последовательность Фибоначчи, где каждое следующие число равно сумме 
#двух предыдущих (1, 1, 2, 3, 5, 8, 13, 21 …), пока новое значение не превысит 444.
print('Задача №5') 
fib1, fib2 = 0, 1
while fib1 + fib2 < 444:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib1 + fib2)
print('\n')
    
#6)	В первый день спортсмен пробежал 10 км, 
# каждый следующий день он увеличивал дистанцию на 20% 
# от дистанции предыдущего дня. Определите, после какого 
# дня суммарный пробег за все дни превысит 500 км и 
# выведите этот пробег.
print('Задача №6') 
a = 10
asum = 0
day = 0
while asum < 500:
    asum +=a
    day += 1
    a = a + a * 0.2
    print(day, round(asum, 3))
print('\n')


#7)	Найдите все трёхзначные и четырёхзначные числа
#  Армстронга. Числом Армстронга считается натуральное
#  число, сумма цифр которого, возведенных в N-ную степень
#  (N – количество цифр в числе) равна самому числу.
#Например, 153 = 13 + 53 + 33.
print('Задача №7') 
start = 100
th = hd = tn = 0
while start <= 9999:
    start += 1
    th = start//1000
    thd = start%1000//100
    tn = start%100//10
    t = start%10
    if th == 0:
        if start == thd**3 + tn**3 + t**3:
            print(start)
    else:
        if start == th**4 + thd**4 + tn**4 + t**4 and start != 10000:
            print(start)