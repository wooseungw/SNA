while(True):
    try:
        a,b,c = map(int, input().split())
        result = max(b-a , c-b)
        print(result-1)
    except:
        break