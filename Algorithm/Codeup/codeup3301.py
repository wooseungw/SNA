money = int(input(""))
man = 0 
chaun = 0
bak = 0
sib = 0
o_man = 0
o_chaun = 0
o_bak = 0
o_sib = 0

def count_5man(man2):
    if  man > 5:
        o_man = man // 5
        man = man - 5 * o_man
    return man, o_man

def count_5chaun(chaun2):
    if  chaun > 5:
        o_chaun = chaun // 5
        chaun = chaun - 5 * o_chaun
    return chaun, o_chaun

def count_5bak(bak2):
    if  bak > 5:
        o_bak = bak // 5
        bak = bak - 5 * o_bak
    return bak, o_bak

def count_5sib(sib2):
    if  sib > 5:
        o_sib = sib // 5
        sib = sib - 5 * o_sib
    return sib, o_sib

if money > 10000:
    man = money // 10000
    money = money - man * 10000
    chaun = money // 1000
    money = money - chaun * 1000
    bak = money // 100
    money = money - bak * 100
    sib = money // 10
    print("{} {} {} {}".format(man,chaun,bak,sib))
    if man >= 5:
        count_5man(man)
        count_5chaun(chaun)
        count_5bak(bak)
        count_5sib(sib)


        
