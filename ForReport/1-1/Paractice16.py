#피클 목표 데이터 가져와 또 쓸 수 있는것, 변수를 외부에 저장할 수 있는 바이너리
import pickle
# profile_file = open("profile.pickle", "wb")#(,바이너리 설정)\
# profile = {"이름":"우승우","나이":23, "취미":["축구","코딩","골프"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile의 정보를 file에저저장 profile.picke 파일이 생김 
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)#file정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# #'with' 파일을 열고 닫고가 편해진다
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.loads(profile_file))#따로 닫을 필요 없이 with문 탈출하면서 끝남
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하고있어요.")
    
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

for i in range(1,51):
    score_file = open("{}주차.txt".format(i), "w", encoding = "utf8")
    print("- {} 주차 주간보고 -".format(i), file=score_file)
    print("부서:", file=score_file)
    print("이름:", file=score_file)
    print("업무 요약:", file=score_file)
    score_file.close()
    
for i in range(1,51):
    with open("{}주차.txt".format(i), "w", encoding = "utf8") as reprot_file:
        reprot_file.write("- {} 주차 주간보고 -".format(i))
        reprot_file.write("부서:")
        reprot_file.write("이름:")
        reprot_file.write("업무 요약:") 