print('Задача №1')
W = {'a': 100, 'b': 500, 'c': 60}
print(W)

print('Задача №2')
keys = []
for key in W:
    keys.append(key)
print(keys)
el = []
for val in W.values():
    el.append(val)
print(el)

print('Задача №3')
id = ['d', 'e', 'f']
val = [400, 789, 350]
Z = dict(zip(id, val))
print(Z)

print('Задача №4')
W.update(Z)
print(W)

print('Задача №5')
print('b' in W, 'p' in W, 'd' in W)

print('Задача №6')
print(len(W))

print('Задача №7')
del W['f']
print(W)

print('Задача №8')
W['a'] = 500
print(W)

print('Задача №9')
T = tuple((k, W[k]) for k in W)
print(T)

print('Задача №10')
W.update(g = 300)
Q = W.copy()
print(Q)
Q.clear()
print(Q)