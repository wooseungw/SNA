

eng_grade = input("영어 성적을 입력하세요:")
eng_grade = int(eng_grade)
math_grade = int(input("수학 성적을 입력하세요:"))

total_grade = math_grade + eng_grade

if total_grade < 110:
    print("불합격 입니다.(사유: 총 점수 부족)")
elif eng_grade >= 40:
    if math_grade >= 40:
        print("합격")
    else:
        print("불합격 입니다.(사유: 수학 점수 부족)")    
else:
    print("불합격 입니다.(사유: 영어 점수 부족)")        