toeic = int(input("토익점수는 몇점인가요? "))
grade = float(input("학점은 몇점인가요? "))

if toeic >= 600 and grade >= 3.0 :
    print("서류 전형에 합격하였습니다.")
else :
    print("서류 전형에 불합격하였습니다.")