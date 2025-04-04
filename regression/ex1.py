# 예제 1
import numpy as np

scores = [88, 92, 75, 100, 89, 95, 73, 68, 85, 90, 78, 82, 96, 87, 91]
print("1. Numpy 배열 생성")
scores = np.array(scores)
print(scores)
print("2. Numpy 메소드를 이용해서 값을 구하시오.")
print("mean:", np.mean(scores), ", min:", np.min(scores), ", max:", np.max(scores), ", median:", np.median(scores))
print("3. 다음의 조건을 구하시오.")
print("Over 80: ", scores[scores > 80])
print("Under 70 Count:  ", len(scores[scores < 70]))
print("Sort:    ", np.sort(scores))
print("Plus 5:  ", scores + 5)