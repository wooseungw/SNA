
front, back = input().split("-")


if back[:1] == "1" :
    gender = 'M'
    print("19{}/{}/{} {}".format(front[:2],front[2:4],front[4:],gender))
elif  back[:1] == "3":
    gender = 'M'
    print("20{}/{}/{} {}".format(front[:2],front[2:4],front[4:],gender))
elif back[:1] == "2": 
    gender = 'F'
    print("19{}/{}/{} {}".format(front[:2],front[2:4],front[4:],gender))
elif back[:1] == "4":
    gender = 'F'
    print("20{}/{}/{} {}".format(front[:2],front[2:4],front[4:],gender))
    
