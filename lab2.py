import math
x = int(input()) #почему-то не работает ввод
exp = math.floor(math.sqrt(math.fabs(math.exp(x) + math.factorial(x)*math.pi)))
print(x,'\n', exp)
lg = math.ceil(math.pow((math.log10(x) + math.sqrt(math.pow(x, 3))), x-2))
print(lg)
sin = x**math.e+(math.sin(x*math.pi)/math.tan(x**-1))
print(sin)



cos = round(math.cos(x), 2)
print(cos)

y = int(input())
cos = math.cos(y)
sin = 1 - math.cos(y)**2
print('sin^2(y) + cos^2(y) = {} + {} = 1'.format(round(sin, 2), round(cos**2, 2)))



interval = int(input())
interval = -10 <= interval <= 10
print(interval)

x1 = int(input())
x2 = int(input())
x3 = int(input())
print(max(x1, x2, x3))

even_odd = int(input())
even_odd = even_odd % 2 == 0
print(even_odd)

a1 = int(input())
a2 = int(input())
c = max(a1, a2)
a1 = min(a1, a2)
print(c - a1)