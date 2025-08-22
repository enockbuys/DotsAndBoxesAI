import pygame
import sys
from config import *
from board import Board
from player import get_clicked_line
from ai_agent import AIAgent
from ui import draw_board, draw_scores
from learning_log import show_agent_learning
pygame.init()

def main():
    win_history = {"Human": 0, "AI": 0}
    game_count = 0
    grid_size = min(int(input("Enter grid size (3 - 15): ")), 15)
    board = Board(grid_size)
    ai = AIAgent()

    width = height = margin * 2 + grid_size * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dots and Boxes")
    font = pygame.font.SysFont(None, 30)

    turn = "Human"
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(screen_color)
        draw_board(screen, board)
        draw_scores(screen, board, font)
        pygame.display.flip()

        if board.is_game_over():
            ai_score = board.scores.get("AI", 0)
            human_score = board.scores.get("Human", 0)
            winner = "AI" if ai_score > human_score else "Human"
            win_history[winner] += 1
            game_count += 1
            print(f"Game {game_count}: Winner = {winner}")
            print(f"Score => Human: {board.scores['Human']} | AI: {board.scores['AI']}")
            print(f"AI Wins: {win_history['AI']} / {game_count}")
            with open("learning_progress.txt", "a") as f:
                f.write(f"Game {game_count}: Winner = {winner}, Q-table Size = {len(ai.q_table)}\n")
            show_agent_learning(ai)
            ai.save()
            ai.epsilon = max(0.01, ai.epsilon * 0.995)
            pygame.time.wait(3000)
            board.reset_board()
            turn = "Human"
            continue

        if turn == "Human":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    ai.save()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    move = get_clicked_line(pygame.mouse.get_pos(), grid_size)
                    if move and board.is_valid_move(move):
                        completed = board.draw_line(move, "Human")
                        turn = "Human" if completed else "AI"
        else:
            pygame.time.wait(ai_delay)
            move = ai.choose_move(board)
            completed = board.draw_line(move, "AI")
            reward = 1 if completed else 0
            ai.learn(board, reward)
            turn = "AI" if completed else "Human"

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()