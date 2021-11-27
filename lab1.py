a = 10
b = 30
a = 8
x = 0
c = a^b
print(a, b, c)
type(c)
float(a)
b = -6.8
print(a, b, c)
abs = abs(int(b))
mod = b//a
div = round(b%c)
max(a, b, c)
min(a, b, c)
print (oct(a), oct(int(b)), oct(c))

D = "   My name is   "
D = D.strip()
L = D + ' Malcev Danila'
l = len(L)
print(L, '=>', l)
print(D,'\nMalcev Danila')
print(L.replace(" ","\t"))
L = L.replace("\t", " ")
while x < 8:
    print(L)
    x += 1
L = L.upper()
print(L.isupper())
L = L.lower()
L = L.title()
print(L)
spl = L.upper()
L = spl.split()[1]
print(L)
L = L.lower()
print(L.find("m") + 1)
print(L.find("i") + 1)
print(L.find("t") + 1)
L = L.replace("na", "****")
print(L)
print(D.find("y") + 1)

E = "a1 a2 a3"
E = E.split(' ',1)
print(E)
E = ", ".join(E)
print(E)
E = E.rsplit(',', 1)
print(E)