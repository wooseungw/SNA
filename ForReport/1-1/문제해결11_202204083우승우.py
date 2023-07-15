def area_of_circle(r):
    result = 3.14 * r ** 2
    return result

r = int(input("반지름:"))
area = area_of_circle(r) 
print("원의 넓이는 {}입니다.".format(area))