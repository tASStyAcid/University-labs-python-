import copy
print('Задача №1')
x = [5, 3, 6, 8, 3, 4, 6, 2, 1, 4, 5, 6, 7, 7]
# x = []
# i = 0
# N = int(input())
# while i < N:
#     x.append(int(input()))
#     i += 1
print(x)

print('Задача №2') 
y = [12, 1, 6, 7, 3, 22, 6, 2, 17, 4, 5, 67, 3, 9]
# y = []
# i = 0
# N = int(input())
# while i < N:
#     y.append(int(input()))
#     i += 1
print(y)

print('Задача №3')
x = list(set(x))
print(x)

print('Задача №4')
x = set(x)
print(x)
y = set(y)
print(y)

print('Задача №5')
print(len(y))

print('Задача №6')
print(5 in x,  8 in x, 12 in x, 9 in x)

print('Задача №7')
x.add(9)
print(x)

print('Задача №8')
x1 = copy.deepcopy(x)
x2 = copy.deepcopy(x)
x1.discard(8)
print(x1)
x1.discard(12)
print(x1)
x2.remove(8)
print(x2)
# x2.remove(12)
# print(x2)

print('Задача №9')
w = x.union(y)
print(w)

print('Задача №10')
same_d = x.intersection(y)
print(same_d)

print('Задача №11')
not_inc_d = x.difference(y)
print(not_inc_d)

print('Задача №12')
dif_d = x.symmetric_difference(y)
print(dif_d)

print('Задача №13')
print(x.issubset(w))

print('Задача №14')
print(x.issuperset(y))

print('Задача №15')
print(x==y)

print('Задача №16')
print(x>y)

print('Задача №17')
x = frozenset(x)
x.add(19)
print(x)






























