# Load the model
import joblib
import pandas as pd
from sklearn.datasets import load_iris
# Load the iris dataset
iris = load_iris()
loaded_clf = joblib.load('decision_tree_model.pkl')
while True:
    print("붓꽃 판별기:")
    sepal_length = float(input("꽃받침 길이(cm)를 입력하세요(4.3~7.9 cm): "))
    sepal_width = float(input("꽃받침 너비(cm)를 입력하세요(2.0~4.4): "))
    petal_length = float(input("꽃잎 길이(cm)를 입력하세요(1.0~6.9): "))
    petal_width = float(input("꽃잎 너비(cm)를 입력하세요(0.1~2.5): "))
    
    # 입력데이터 시리즈로 변환
    sample = pd.Series([sepal_length, sepal_width, petal_length, petal_width], 
                        index=iris.feature_names)
    
    # 예측 수행
    prediction = loaded_clf.predict([sample])[0]
    
    # 예측 결과 출력
    print(f"Predicted species: {iris.target_names[prediction]}")
    
    continue_prediction = input("Predict another? (y/n): ")
    if continue_prediction.lower() != 'y':
        break
