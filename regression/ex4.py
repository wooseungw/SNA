#예제 4
import numpy as np

cost_price = [12000, 8500, 15000, 9900, 21000, 30000, 17500, 19900, 12500, 28000]
sell_price = [15000, 10000, 18000, 12000, 25000, 35000, 21000, 23000, 15500, 31000]
cost_price = np.array(cost_price)
sell_price = np.array(sell_price)

print("1. 각 제품의 이익(판매가 - 원가)을 구하고, 가장 높은 이익을 내는 제품을 찾으시오.(제품의 색인값과 이익 출력)")
profit = sell_price - cost_price
print("이익:", profit)
print("가장 높은 이익을 내는 제품:", np.argmax(profit), "이익:", np.max(profit))
print("2. 평균 이익률(이익 / 원가 * 100)을 구하시오.")
profit_rate = (profit / cost_price) * 100
print("평균 이익률:", np.mean(profit_rate), "%")
print("3. 원가가 15,000원 이하인 제품 중 이익이 3,000원 이상인 제품을 찾으시오.(제품의 색인값 출력)")
mask = (cost_price <= 15000) & (profit >= 3000)
print(np.where(mask)[0])
print("4. 20,000원 이상인 제품의 판매가를 15% 할인했을 때, 할인 후 가격이 18,000원 이상인 제품만출력하시오. (제품의 색인값 출력)")
mask = (sell_price >= 20000) & ((sell_price * 0.85) >= 18000)
print(np.where(mask)[0])