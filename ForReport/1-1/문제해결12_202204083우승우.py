score_list = [3.1, 3.4, 2.7, 4.1, 4.4]

def minScore(data):
    result = data[0]
    for i in data:
        if i < result:
            result = i
    return result

print("가장 낮은 학점은 {} 입니다.".format(minScore(score_list)))