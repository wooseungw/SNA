first = int(input("초항은? "))
maxNum = int(input("최댓값은? "))
diff = int(input("공차는? "))
for N in range(first, maxNum, diff):
    print(N)