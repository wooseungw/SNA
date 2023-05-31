from pprint import pprint


list = ["apple,","banana","wefwe",2,3,41,15,21,1,"dfwe",2123,"12312fff"]
list_num = []
list_str = []
for i in list:
    if type(i) == int:
        print("{}는 숫자입니다.".format(i))
        list_num.append(i)
    else:
        print("{}는 문자열입니다.".format(i))
        list_str.append(i)
        
print(list_num)
print(list_str)