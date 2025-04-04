#예제 2
import numpy as np
class_A = [78, 85, 90, 88, 76, 95, 89, 84, 91, 87, 80, 93, 72, 99, 83, 77, 94, 86, 81, 79]
class_B = [82, 79, 88, 92, 75, 89, 90, 80, 86, 85, 78, 96, 74, 100, 82, 76, 97, 84, 83, 81]

class_A = np.array(class_A)
class_B = np.array(class_B)
print("두 반의 평균 점수를 비교하고, 어느 반의 평균이 더 높은지 출력하시오")
print("Class A 평균 점수:", np.mean(class_A),"Class B 평균 점수:", np.mean(class_B))
print("Class A"if np.mean(class_A) > np.mean(class_B) else "Class B")
print("두 반의 중앙값과 표준 편차(Standard Deviation)를 구하시오")
print("Class A 중앙값:", np.median(class_A), ", 표준 편차:", np.std(class_A))
print("두 반의 최상위 5명의 점수를 비교하여, 어느 반이 더 높은 점수를 가졌는지 분석하시오.")
print("Class A Top 5:", np.sort(class_A)[-5:], ", Class B Top 5:", np.sort(class_B)[-5:])
print("Class A" if np.mean(np.sort(class_A)[-5:]) > np.mean(np.sort(class_B)[-5:]) else "Class B")
print("반별 80점 이상인 학생의 비율을 계산하고, 더 높은 비율을 가진 반을 출력하시오.")
print("Class A 80점 이상 비율:", len(class_A[class_A >= 80]) / len(class_A) * 100, "%")
print("Class B 80점 이상 비율:", len(class_B[class_B >= 80]) / len(class_B) * 100, "%")
print("Class A" if len(class_A[class_A >= 80]) / len(class_A) > len(class_B[class_B >= 80]) / len(class_B) else "Class B")