import random
import pickle
import os

class AIAgent:
    def __init__(self, name="AI"):
        self.name = name
        self.q_table = {}
        self.last_state = None
        self.last_action = None
        self.epsilon = 0.3
        self.alpha = 0.7
        self.gamma = 0.95
        self.load()

    def get_state_key(self, board):
        flat_h = sum(board.h_lines, [])
        flat_v = sum(board.v_lines, [])
        score_diff = board.scores.get(self.name, 0) - board.scores.get("Human", 0)
        boxes_with_3_sides = sum(
            1 for r in range(board.grid_size) for c in range(board.grid_size)
            if board.boxes[r][c] is None and (
                board.h_lines[r][c] +
                board.h_lines[r+1][c] +
                board.v_lines[r][c] +
                board.v_lines[r][c+1]
            ) == 3
        )
        return tuple(flat_h + flat_v + [score_diff, boxes_with_3_sides])

    def choose_move(self, board):
        state = self.get_state_key(board)
        valid_moves = board.moves
        if random.random() < self.epsilon or state not in self.q_table:
            move = random.choice(valid_moves)
        else:
            q_vals = self.q_table[state]
            move = max(q_vals, key=q_vals.get)
        self.last_state = state
        self.last_action = move
        return move

    def learn(self, board, reward):
        new_state = self.get_state_key(board)
        if self.last_state is None or self.last_action is None:
            return
        self.q_table.setdefault(self.last_state, {})
        self.q_table[self.last_state].setdefault(self.last_action, 0)
        future_q = max(self.q_table.get(new_state, {}).values(), default=0)
        old_q = self.q_table[self.last_state][self.last_action]
        self.q_table[self.last_state][self.last_action] = old_q + self.alpha * (reward + self.gamma * future_q - old_q)

    def save(self):
        with open(f"q_table_{self.name}.pkl", "wb") as f:
            pickle.dump(self.q_table, f)

    def load(self):
        fname = f"q_table_{self.name}.pkl"
        if os.path.exists(fname):
            with open(fname, "rb") as f:
                self.q_table = pickle.load(f)