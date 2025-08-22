class Board:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.reset_board()

    def reset_board(self):
        self.h_lines = [[False]*self.grid_size for _ in range(self.grid_size+1)]
        self.v_lines = [[False]*(self.grid_size+1) for _ in range(self.grid_size)]
        self.boxes = [[None]*self.grid_size for _ in range(self.grid_size)]
        self.scores = {}
        self.moves = self.get_all_moves()

    def get_all_moves(self):
        moves = []
        for r in range(self.grid_size + 1):
            for c in range(self.grid_size):
                moves.append(('h', r, c))
        for r in range(self.grid_size):
            for c in range(self.grid_size + 1):
                moves.append(('v', r, c))
        return moves

    def is_valid_move(self, move):
        dir, r, c = move
        return not (self.h_lines[r][c] if dir == 'h' else self.v_lines[r][c])

    def draw_line(self, move, player):
        dir, r, c = move
        if dir == 'h':
            self.h_lines[r][c] = True
        else:
            self.v_lines[r][c] = True

        completed_boxes = self.check_boxes(player)
        if completed_boxes:
            if player not in self.scores:
                self.scores[player] = 0
            self.scores[player] += len(completed_boxes)

        self.moves.remove(move)
        return bool(completed_boxes)

    def check_boxes(self, player):
        completed = []
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.boxes[r][c] is None:
                    if self.h_lines[r][c] and self.h_lines[r+1][c] and self.v_lines[r][c] and self.v_lines[r][c+1]:
                        self.boxes[r][c] = player
                        completed.append((r, c))
        return completed

    def is_game_over(self):
        return len(self.moves) == 0