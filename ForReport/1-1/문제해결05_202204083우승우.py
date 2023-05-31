score = int(input("점수를 입력하세요 "))
if score < 0 :
    print("ERROR(음수)")
elif score <= 100 :
    if score >= 60 :
        print("PASS")
    else :
        print("FAIL")
else :
    print("ERROR(100 초과)")