import copy
import math
#vector = [0] * int(input())
#for i in range(len(vector)):
#    vector[i] = int(input())
v = [2, 3, 4, 2, 3, 2, 3, 4, 1, 1, 1, 5, 6, 6, 6]
print(v)
v.extend((5, 7, 8))
print(v)
v.sort()
print(v)
print(v[4:8])
print(v[3:9])
print(v[2], v[4], v[11])
v.remove(v[3])
print(v)
v.insert(1, 6)
if 9 in v or 1 in v:
    print('Входит 1 или 9')
x = copy.deepcopy(v)
print(v,'\n' , x)
reversed(x)
x.remove(x[len(x)-1])
print(x)
x.insert(4, 12)
print(x)
x.remove(x[4]) ; x.remove(x[2])
print(x)
x.extend(v)
print(x*3)
print(x.count(6))
print(', '.join(map(str, x)))
print('_'.join(map(str, x)))
print('/'.join(map(str, x)))
for i in range(len(x)):
    print(math.sqrt(x[i]))
print(max(x), min(x))
y = [i for i in range(3, 16)]
print(y)
z = [i for i in range(3, 21)]
print(z[::-1])