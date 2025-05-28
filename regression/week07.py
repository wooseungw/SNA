# 필요한 라이브러리 가져오기
from sklearn.datasets import load_iris  # iris 데이터셋을 불러오기 위함
from sklearn.tree import DecisionTreeClassifier  # 결정 트리 모델을 생성하기 위함
from sklearn.model_selection import train_test_split  # 데이터를 훈련 및 검증 세트로 분할하기 위함
import pandas as pd  # 데이터 조작을 위함
import joblib  # 훈련된 모델을 저장하기 위함

# iris 데이터셋 불러오기
iris = load_iris()

# 더 나은 시각화를 위해 iris 데이터를 pandas DataFrame으로 변환
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# 타겟 클래스 이름(iris 품종) 출력
print(iris.target_names)
# DataFrame에 타겟 열 추가
iris_df['target'] = iris.target
# DataFrame의 처음 5행 표시
print(iris_df.head())

# 데이터를 훈련 및 검증 세트로 분할 (80% 훈련, 20% 검증)
x_t ,x_v, y_t, y_v = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
# 재현성을 위해 랜덤 상태를 설정하여 결정 트리 분류기 초기화
clf = DecisionTreeClassifier(random_state=42)
# 훈련 데이터로 분류기 학습
clf.fit(x_t, y_t)
# 검증 데이터에 대해 예측 수행
pred = clf.predict(x_v)
# 처음 5개 예측 결과 표시
pred[:5]
# 나중에 사용하기 위해 훈련된 모델을 파일로 저장
joblib.dump(clf, 'decision_tree_model.pkl')
