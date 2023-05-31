totalprice = int(input("소비자가격은?:"))

def cal_productPirce(totalPrice):
    productPrice = totalPrice * 10 / 11
    return productPrice

def cal_tax(totalPrice) :
    tax = totalPrice / 11
    return tax


print("제품 가격은 {}".format(cal_productPirce(totalprice)))
print("부가가치세는 {}".format(cal_tax(totalprice)))
