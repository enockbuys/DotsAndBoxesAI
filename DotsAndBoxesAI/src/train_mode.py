from board import Board
from ai_agent import AIAgent

def train_ai(num_games=5000, grid_size=3):
    shared_ai = AIAgent(name="AI")

    for game in range(num_games):
        board = Board(grid_size)
        turn = "AI1"

        while not board.is_game_over():
            move = shared_ai.choose_move(board)
            completed = board.draw_line(move, turn)
            reward = 1 if completed else -0.1
            shared_ai.learn(board, reward)
            turn = turn if completed else ("AI2" if turn == "AI1" else "AI1")

        shared_ai.epsilon = max(0.01, shared_ai.epsilon * 0.995)
        if game % 500 == 0 or game == num_games:
            shared_ai.save()
        with open("learning_progress.txt", "a") as log:
            log.write(f"Game {game}: Q-table size = {len(shared_ai.q_table)}, Epsilon = {shared_ai.epsilon:.4f}\n")
        print(f"Game {game+1} completed.")

if __name__ == "__main__":
    train_ai()