#예제 3
import numpy as np
# 4개 도시(서울, 부산, 대구, 광주)의 1주일 기온 데이터
city_temps = [
[12.3, 14.1, 15.8, 13.5, 16.2, 17.0, 14.8], # 서울
 [15.2, 16.8, 18.1, 17.4, 19.0, 20.5, 18.6], # 부산
 [14.5, 15.9, 17.3, 16.0, 18.2, 19.8, 17.5], # 대구
 [13.8, 15.2, 16.5, 14.9, 17.0, 18.3, 16.1] # 광주
]
city_temps = np.array(city_temps)
print("1. 4개 도시의 7일간 평균 기온")
print("서울:", np.mean(city_temps[0]), "부산:", np.mean(city_temps[1]), "대구:", np.mean(city_temps[2]), "광주:", np.mean(city_temps[3]))
print("2. 각 도시별 최저 및 최고 기온")
print("서울: 최저", np.min(city_temps[0]), "최고", np.max(city_temps[0]), 
    "부산: 최저", np.min(city_temps[1]), "최고", np.max(city_temps[1]), 
    "대구: 최저", np.min(city_temps[2]), "최고", np.max(city_temps[2]), 
    "광주: 최저", np.min(city_temps[3]), "최고", np.max(city_temps[3]))
print("3. 일주일 동안 전국 평균 기온")
print(np.mean(city_temps, axis=0))
print("4. 평균 기온이 16도 이상인 날과, 해당 날짜의 모든 도시 기온")
print("서울:", city_temps[0][city_temps[0] >= 16])
print("부산:", city_temps[1][city_temps[1] >= 16])
print("대구:", city_temps[2][city_temps[2] >= 16])
print("광주:", city_temps[3][city_temps[3] >= 16])
print("5.모든 기온을 화씨로 변환")
print(city_temps * 9/5 + 32)
print("6. 가장 기온 변화가 심한 도시")
print("서울:", np.max(city_temps[0]) - np.min(city_temps[0]))
print("부산:", np.max(city_temps[1]) - np.min(city_temps[1]))
print("대구:", np.max(city_temps[2]) - np.min(city_temps[2]))
print("광주:", np.max(city_temps[3]) - np.min(city_temps[3]))
