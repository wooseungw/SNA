i, j = input("").split( )
i = int(i)
j = int(j)

for a in range(i):
    a = 1 + a
    for b in range(j):
        b = 1 + b 
        print("{} {}".format(a,b))
    