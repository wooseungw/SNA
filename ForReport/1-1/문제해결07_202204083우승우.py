lectures = {"컴퓨터프로그래밍":3, "선형대수학" :3, "유튜브제작" :3,"현대철학개론":2,"대학국어":2}   
lectures_name = input("과목명? ")

print("{}의 학점은 {}점입니다.".format(lectures_name,lectures[lectures_name]))