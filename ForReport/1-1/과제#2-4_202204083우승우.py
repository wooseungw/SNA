def factorical(x):
    if x ==0:
        return 1
    else:
        return x * factorical(x-1)
    
print(factorical(5))