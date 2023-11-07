# 행동 가치 함수
def action_value_function(env, agent, act, G, max_step, now_step):   
    
    # 1. 감가율 설정
    gamma = 0.9
    
    # 2. 현재 위치가 목적지인지 확인
    if env.reward_list1[agent.pos[0]][agent.pos[1]] == "goal":
        return env.goal

    # 3. 마지막 상태는 보상만 계산
    if (max_step == now_step):
        observation, reward, done = env.move(agent, act)
        G += agent.select_action_pr[act]*reward
        return G
    
    # 4. 현재 상태의 보상을 계산한 후 다음 행동과 함께 다음 step으로 이동
    else:
        # 4.1현재 위치 저장
        pos1 = agent.get_pos()
        observation, reward, done = env.move(agent, act)
        G += agent.select_action_pr[act] * reward
        
        # 4.2 이동 후 위치 확인 : 미로밖, 벽, 구멍인 경우 이동전 좌표로 다시 이동
        if done == True:            
            if observation[0] < 0 or observation[0] >= env.reward.shape[0] or observation[1] < 0 or observation[1] >= env.reward.shape[1]:
                agent.set_pos(pos1)
            
        # 4.3 현재 위치를 다시 저장
        pos1 = agent.get_pos()
        
        # 4.4 현재 위치에서 가능한 모든 행동을 선택한 후 이동
        for i in range(len(agent.action)):
            agent.set_pos(pos1)
            next_v = action_value_function(env, agent, i, 0, max_step, now_step+1)
            G += agent.select_action_pr[i] * gamma * next_v
        return G
