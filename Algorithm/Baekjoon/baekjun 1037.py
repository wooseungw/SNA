import sys

num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split(" ")))
num_list.sort()
print(num_list[0]*num_list[num-1])
