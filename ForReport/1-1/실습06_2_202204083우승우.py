grade = int(input("성적을 입력하세요:"))

if grade >= 90:
    print("A학점 입니다.")
elif 90 > grade >= 80:
    print("B학점 입니다.")
elif 80 > grade >= 70:
    print("C학점 입니다.")    
else:
    print("D학점 입니다.")