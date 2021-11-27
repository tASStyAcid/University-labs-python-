# 1.	Вывести на экран циклом пять строк из нулей, 
# причем каждая строка должна быть пронумерована;
print('Задача №1') 
i = 0
while i < 5:
    print(i+1 ,'0')
    i += 1
print('\n')

# 2.	Найти сумму ряда чисел от 1 до 100. 
# Полученный результат вывести на экран;
print('Задача №2') 
a = 1
sum = 0
while a<=100:
    sum += a
    a += 1
print(sum)
print('\n')

# 3.	Дано семь чисел. Найти количество положительных чисел 
# среди них:
# 3.1.	5964, -12, -68874, 101, -103, -741, 36985
# 3.2.	-713, -12563, -89, -45698, -898, -75632, -635
print('Задача №3') 
p = []
i = j = pos = 0
n = int(input())
while i < n:
    p.append(int(input()))
    i += 1
for j in range(n):
    if p[j] >= 0:
        pos += 1
print(pos, p, '\n')
print('\n')

# 4.	Даны три числа. Вывести на экран «yes«, если 
# среди них есть одинаковые, иначе вывести “ERROR”:
# 4.1.	956820, 956620, 936820
# 4.2.	24930566, 24960566, 24930566
# 4.3.	3496, 3496, 3496
print('Задача №4') 
arr = []
i = 0
N = int(input())
while i < N:
    arr.append(int(input()))
    i += 1
for i in range(N-1):
    if arr[i] == arr[i+1]:
        print("Yes")
        break
else:
    print("Error")
print('\n')

# 5.	Даны три числа. Вывести на экран «yes«, если 
# можно взять какие-то два из них и в сумме получить третье:
# 5.1.	9760, 3594, 6166
# 5.2.	56783, 49998, 6784
print('Задача №5') 
arr = []
i = sum = j = 0
N = int(input())
while i < N:
    arr.append(int(input()))
    i += 1
for j in range(N-1):
    sum += arr[j]
if sum == arr[N-1]:
    print('Yes')
else:
    print('No')
print('\n')

# 6.	Вывести на экран все чётные значения в диапазоне 
# от 1 до 698;
print('Задача №6') 
N = int(input())
i = 2
arr = []
for i in range(N+1):
    if i%2 == 0:
        arr.append(i)
print(arr[1:])
print('\n')

# 7.	Посчитать сумму числового ряда:
# 7.1.	от 0 до 14,например, 0+1+2+3+…+14
# 7.2.	от 569 до 601 
# 7.3.	от -65 до 12
print('Задача №7') 
x1 = int(input())
x2 = int(input())
i = sum = 0 
for i in range(x1, x2+1):
    sum += i
print(sum)
print('\n')

# 8.	Перемножить все не чётные значения в диапазоне от 0 до 84;
print('Задача №8') 
x1 = int(input())
x2 = int(input())
i = 0
mult = 1
for i in range(x1, x2+1):
    if i%2 != 0:
        mult *= i
print(mult)
print('\n')

# 9.	Записать в массив все числа в диапазоне от 54 до 3945 
# кратные 5;
print('Задача №9') 
x1 = int(input())
x2 = int(input())
arr = []
while x1 <= x2:
    if x1%5 != 0:
        x1 += 1
    arr.append(x1)
    x1 += 5
print(arr)