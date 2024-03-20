def printPoly(p_x):
    term = len(px)-1
    poltStr = "P(x) = "
    
    for i in range(len(p_x)):
        coef = p_x[i]
        if (coef > 0 and i > 0):
            poltStr += "+"
        if coef != 0:
            if term ==0 :
                poltStr += str(coef)
            else:
                poltStr += str(coef) + "x^" + str(term)+ " "
        term -= 1
        
    return poltStr

def cal(xVal,p_x):
    returnValue =0
    term = len(px)-1
    for i in range(len(px)):
        coef = p_x[i]
        returnValue += coef*xVal **term
        term -= 1
    return returnValue

if __name__ =="__main__":
    px = [4,-2,0,4,-5]

    print(printPoly(px))
    xVal = int(input("x: ?"))
    print(cal(xVal,px))
