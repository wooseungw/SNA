def password_check(password):
    result = ""
    if len(password) < 5:
        result = "bad"
    elif 5 < len(password) < 9:
        result = "Normal"
    else:
        result = "good"
    return result
        
password = input("패스워드 입력: ")
print("당신의 패스워드: {}".format(password_check(password)))