import numpy as np
import matplotlib.pyplot as plt
from Draw import *
from StateActionFunc import *
from Environment import *
from Agent import *

# 재귀적으로 행동의 가치를 계산

# 1. 환경 초기화
env = Environment()

# 2. 에이전트 초기화
agent = Agent()
np.random.seed(0)

# 3. 현재부터 max_step 까지 계산
max_step_number = 8

# 4. 모든 상태에 대해
for max_step in range(max_step_number):
    # 4.1 미로 상의 모든 상태에서 가능한 행동의 가치를 저장할 테이블을 정의
    print("max_step = {}".format(max_step))
    q_table = np.zeros((env.reward.shape[0], env.reward.shape[1],len(agent.action)))
    for i in range(env.reward.shape[0]):
        for j in range(env.reward.shape[1]):
            # 4.2 모든 행동에 대해
            for action in range(len(agent.action)):
                # 4.2.1 에이전트의 위치를 초기화
                agent.set_pos([i,j])
                # 4.2.2 현재 위치에서 행동 가치를 계산
                q_table[i ,j,action] = action_value_function(env, agent, action, 0, max_step, 0)

    q = np.round(q_table,2)
    print("Q - table")
    show_q_table(q, env)
    print("High actions Arrow")
    show_q_table_arrow(q,env)
    print()
    