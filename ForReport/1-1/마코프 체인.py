Sunny = [0.25]
Rain = [0.25]
Cloud = [0.25]
Snow = [0.25]


for i in range(1, 100):
    Sunny.append(round(Sunny[i-1]* 0.5 + Rain[i-1]*0.2 + Cloud[i-1]*0.2+ Snow[i-1]*0.2, 6))
    Rain.append(round(Sunny[i-1]* 0.1 + Rain[i-1]*0.3 + Cloud[i-1]*0.3+ Snow[i-1]*0.1, 6))
    Cloud.append(round(Sunny[i-1]* 0.3 + Rain[i-1]*0.4 + Cloud[i-1]*0.3+ Snow[i-1]*0.4, 6))
    Snow.append(round(Sunny[i-1]* 0.1 + Rain[i-1]*0.1 + Cloud[i-1]*0.2+ Snow[i-1]*0.3, 6))
    
    if abs(Sunny[i] - Sunny[i-1]) >= 0.00001 or abs(Rain[i] - Rain[i-1]) >= 0.00001:
        print("맑음:{:.5f} 비:{:.5f} 흐림:{:.5f} 눈:{:.5f}".format(Sunny[i],Rain[i],Cloud[i],Snow[i]))
    else:    
        print("count: {}".format(i)) 
        break
        
         
    