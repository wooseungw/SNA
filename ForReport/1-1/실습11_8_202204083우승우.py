bottom_lenght = int(input("밑변의 길이는?: "))
height_lenght = int(input("높이의 길이는?: "))

def cal_area(bottom, height):
    area = float(0.5 * bottom * height)
    return area

print("삼각형의 넓이:{}".format(cal_area(bottom_lenght,height_lenght)))