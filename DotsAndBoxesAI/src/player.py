from config import *

def get_clicked_line(pos, grid_size):
    x, y = pos
    for r in range(grid_size + 1):
        for c in range(grid_size):
            x1 = margin + c * cell_size
            y1 = margin + r * cell_size
            if abs(x - (x1 + cell_size // 2)) < cell_size // 2 and abs(y - y1) < 10:
                return ('h', r, c)
    for r in range(grid_size):
        for c in range(grid_size + 1):
            x1 = margin + c * cell_size
            y1 = margin + r * cell_size
            if abs(x - x1) < 10 and abs(y - (y1 + cell_size // 2)) < cell_size // 2:
                return ('v', r, c)
    return None
