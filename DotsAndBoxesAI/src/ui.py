import pygame
from config import *

def draw_board(screen, board):
    screen.fill(screen_color)
    for r in range(board.grid_size + 1):
        for c in range(board.grid_size + 1):
            x = margin + c * cell_size
            y = margin + r * cell_size
            pygame.draw.circle(screen, dot_color, (x, y), dot_radius)
    for r in range(board.grid_size + 1):
        for c in range(board.grid_size):
            if board.h_lines[r][c]:
                x = margin + c * cell_size
                y = margin + r * cell_size
                pygame.draw.line(screen, line_color, (x, y), (x + cell_size, y), line_width)
    for r in range(board.grid_size):
        for c in range(board.grid_size + 1):
            if board.v_lines[r][c]:
                x = margin + c * cell_size
                y = margin + r * cell_size
                pygame.draw.line(screen, line_color, (x, y), (x, y + cell_size), line_width)
    for r in range(board.grid_size):
        for c in range(board.grid_size):
            if board.boxes[r][c]:
                x = margin + c * cell_size + 5
                y = margin + r * cell_size + 5
                rect = pygame.Rect(x, y, cell_size - 10, cell_size - 10)
                color = player_color if board.boxes[r][c] == "Human" else ai_color
                pygame.draw.rect(screen, color, rect)

def draw_scores(screen, board, font):
    human = board.scores.get("Human", 0)
    ai = board.scores.get("AI", 0)
    text = font.render(f"Human: {human} | AI: {ai}", True, (0, 0, 0))
    screen.blit(text, (margin, 10))