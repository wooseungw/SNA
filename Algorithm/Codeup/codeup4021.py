a,b,c,d,e,f,g = input("").split( )
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)

k = [a,b,c,d,e,f,g]
g = []

for i in k:
    if i % 2 == 1:
      g.append(i)

if sum(g) == 0:
    print(-1)
else:
    print(sum(g))  


