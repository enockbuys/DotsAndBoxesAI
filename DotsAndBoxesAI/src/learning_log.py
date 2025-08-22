def show_agent_learning(agent):
    print("Learning Status:")
    print(f"Q-table Size: {len(agent.q_table)}")
    if agent.last_state:
        print(f"Last move: {agent.last_action}")
        print(f"Last state hash: {hash(agent.last_state)}")
        if agent.last_state in agent.q_table:
            print("Recent Q-values:")
            for move, q in agent.q_table[agent.last_state].items():
                print(f"{move}: Q = {q:.3f}")