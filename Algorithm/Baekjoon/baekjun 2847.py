import sys

n = int(sys.stdin.readline())
score = []
for i in range(n):
    score.append(int(sys.stdin.readline()))

print(score)

len_score = len(score)

max_value = score[len_score -1]
for i in range(0,len_score-1,-1):
    
    if score[i-1]