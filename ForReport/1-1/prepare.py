# age= int(input("나이:"))

# if age >= 20:
#     print("당신은 어른이다.")
# else:
#     print("ekdtlsdms ")
# coin = input("동전은 면: ")

# if coin == "앞면":
#     print("중국요리 먹어라")
# else:
#     print("일본요리 먹어라")
    
# shirt = int(input("셔츠는 몇벌?:"))
# shrit_price = shirt*10000
# sweater = int(input("스웨터는 몇벌?:"))
# sweater_price = sweater * 30000
# price_all = shrit_price + sweater_price

# if price_all >= 100000:
#     price_all = price_all*0.85
#     print("총가격은 {}입니다.".format(price_all))
# else:
#     price_all = price_all*0.95
#     print("총가격은 {}입니다.".format(price_all))

# heigth = int(input("키: ")) 
# weight = int(input("몸무게: "))

# if heigth >= 155 and weight >= 50:
#     print("놀이기구에 탈 수 있습니다.")
# else:
#     print("놀이기구를 탈 수 없습니다.")
    
# score = int(input("토익점수:"))
# grade = float(input("학점:"))

# if score >= 600 and grade >= 3.0:
#     print("서류 전형에 합격 했습니다.")
# else:
#     print("서류 전형에 불합격 했습니다.")

# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
# num3 = int(input("num3:"))

# if num1 >= num2 :
#     if num3 >= num2:
#         print("가장작은수는 {}입니다.".format(num2))
#     else:
#         print("가장 작은수는 {}입니다.".format(num3))
# else:
#     if num1 >= num3:
#         print("가장 작은수는 {}입니다.".format(num3))
#     else:   
#         print("가장 작은수는 {}입니다.".format(num1))

# class Unit:
#     def __init__(self, Name, ID, Password):
#         self.Name = Name
#         self.ID = ID #맴버변수 class내 정의되는 변수,초기화,사용 가능
#         self.Password = Password
#         print("{0}의 계정이 생성되었습니다.".format(self.Name))
#         print("아이디{0}, 비밀번호{1}".format(self.ID, self.Password))
        
# jongsu = Unit("정수","abc","정수123")
# id = (input("아이디:"))
# password = (input("비밀번호:"))

# if len(id) <= 10:
#     if len(password) <= 10 :
#         print("회원가입 완료")
#     else:
#         print("비밀번호 길이가 너무 깁니다.")
# else:
#     print("아이디 길이가 너무 깁니다.")
    
# if id == jongsu.ID:
#     if password == jongsu.Password:
#         print("로그인 완료")
#     else:
#         print("로그인 실패: Password오류")
# else:
#     print("로그인 실패: ID 오류")

# A = int(input("A?: "))
# B = int(input("B?: "))

# if A*B > 0:
#     if B > 0 :
#         print("A,B 모두 양수이다.")
#     else:
#         print("A,B 모두 음수이다.")
# else:
#     if A > 0 :
#         print("A는 양수이다.\nB는 음수이다.")
#     else:
#         print("B는 양수이다.\nA는 음수이다.")
# score = int(input("총 점수:"))

# if score >= 90:
#     print("학점은 A") 
# elif score >= 80:
#     print("학점은 B") 
# elif score >= 70:
#     print("학점은 C") 
# else:
#     print("학점은 D") 
# eng = int(input("영어점수:"))
# mth = int(input("수학점수:"))
# score = eng + mth
# if score < 110:
#     print("총 점수가 부족합니다.")
# elif eng >= 40:
#     print("수학 점수가 부족합니다.")
# elif mth >= 40:
#     print("영어 점수가 부족합니다.")
# else:
#     print("합격.")

list = ["커피",2,3,4,1,2,2,4]
list_ex1 = ["risk","issue","test","maintenance","maturity"]
list_ex2 = ["security","plan","design","systematic","safety","maintenance"]
list_ex3 = ["maintenace","verification","vaildation"]
a= list[0]
print(a)
print("아메리카노" in list)
print("아메리카노" not in list)
print(len(list))

if "maintenance" in list_ex1 and len(list_ex1) >= 5:
    print("가장적합한 시험문제는 ex1이다.")
elif "maintenance" in list_ex2 and len(list_ex2) >= 5:
    print("가장적합한 시험문제는 ex2이다.")
elif "maintenance" in list_ex3 and len(list_ex3) >= 5:
    print("가장적합한 시험문제는 ex3이다.")
    
list_combine = list_ex3 + list_ex2
print(list_combine * 2)
print(list_combine[3:6])
print(list_combine[:6])
print(list_combine[3:])
list_combine[2] = "oao"
print(list_combine)
list_combine[3:] = [1,23,4,51,5,1,23,2]
print(list_combine)
list_combine[:2] = [99,22]
print(list_combine)

list_a = [37, 64, 21, 55, "cat", "japan"]
list_b = [ 23, 55, "dog", "china"]

print(len(list_a))
if "cat" in list_a:
    print("있음")
else:
    print("없음")
print(len(list_b))
if "cat" in list_b:
    print("있음")
else:
    print("없음")