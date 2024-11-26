import numpy as np
import random

class Minimax2048AI:
    def __init__(self, depth=4, alpha=-1e10, beta=1e10, weights=[0.6, 0.1, 0.3, 0.5]):
        self.depth = depth
        self.alpha = alpha
        self.beta = beta
        self.weights = np.array(weights)

    def mat_init(self, input_grid):
        mat = []
        for i in range(4):
            row = []
            for j in range(4):
                if input_grid[i][j] == '':
                    row.append(0)
                else:
                    row.append(int(input_grid[i][j]))
            mat.append(row)
        return np.array(mat)

    def evaluate_board(self, grid):
        smoothness = self.cal_smoothness(grid)
        empty_spaces = self.cal_empty_spaces(grid)
        max_tile = self.cal_maximum_tile(grid)
        monotonicity = self.cal_monotonicity(grid)
        return np.dot(self.weights, [smoothness, empty_spaces, max_tile, monotonicity])

    def cal_smoothness(self, grid):
        smoothness = 0
        for i in range(4):
            for j in range(3):
                if grid[i][j] != 0 and grid[i][j + 1] != 0:
                    smoothness -= abs(np.log2(grid[i][j]) - np.log2(grid[i][j + 1]))
                if grid[j][i] != 0 and grid[j + 1][i] != 0:
                    smoothness -= abs(np.log2(grid[j][i]) - np.log2(grid[j + 1][i]))
        return smoothness

    def cal_empty_spaces(self, grid):
        return np.sum(grid == 0)

    def cal_maximum_tile(self, grid):
        return np.log2(np.max(grid)) if np.max(grid) > 0 else 0

    def cal_monotonicity(self, grid):
        monotonicity = 0
        for row in grid:
            diff = np.diff(np.log2(row[row > 0]))
            monotonicity += np.sum(diff >= 0) - np.sum(diff < 0)
        for col in grid.T:
            diff = np.diff(np.log2(col[col > 0]))
            monotonicity += np.sum(diff >= 0) - np.sum(diff < 0)
        return monotonicity

    def get_possible_moves(self, grid):
        moves = []
        for direction in ["up", "down", "left", "right"]:
            new_grid, changed = self.apply_move(grid, direction)
            if changed:
                moves.append((direction, new_grid))
        return moves

    def apply_move(self, grid, direction):
        def merge(row):
            new_row = [x for x in row if x != 0]
            merged_row = []
            skip = False
            for i in range(len(new_row)):
                if skip:
                    skip = False
                    continue
                if i < len(new_row) - 1 and new_row[i] == new_row[i + 1]:
                    merged_row.append(new_row[i] * 2)
                    skip = True
                else:
                    merged_row.append(new_row[i])
            return merged_row + [0] * (len(row) - len(merged_row))

        rotated = grid.copy()
        if direction == "up":
            rotated = np.rot90(rotated, -1)
        elif direction == "down":
            rotated = np.rot90(rotated, 1)
        elif direction == "right":
            rotated = np.fliplr(rotated)

        new_grid = np.array([merge(row) for row in rotated])
        if direction == "up":
            new_grid = np.rot90(new_grid, 1)
        elif direction == "down":
            new_grid = np.rot90(new_grid, -1)
        elif direction == "right":
            new_grid = np.fliplr(new_grid)

        return new_grid, not np.array_equal(grid, new_grid)

    def generate_random_states(self, grid):
        empty_positions = list(zip(*np.where(grid == 0)))
        random_states = []
        for pos in empty_positions:
            for value in [2, 4]:
                new_grid = grid.copy()
                new_grid[pos] = value
                random_states.append(new_grid)
        return random_states

    def minimax(self, grid, depth, is_ai_turn, alpha, beta):
        if depth == 0 or np.max(grid) >= 2048 or self.cal_empty_spaces(grid) == 0:
            return self.evaluate_board(grid)

        if is_ai_turn:
            max_eval = -np.inf
            for _, new_grid in self.get_possible_moves(grid):
                eval = self.minimax(new_grid, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = np.inf
            for random_grid in self.generate_random_states(grid):
                eval = self.minimax(random_grid, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self, grid):
        best_move = None
        best_value = -np.inf
        for move, new_grid in self.get_possible_moves(grid):
            value = self.minimax(new_grid, self.depth - 1, False, self.alpha, self.beta)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

# Example usage
if __name__ == "__main__":
    # Example initial grid
    initial_grid = np.array([
        [2, 0, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])
    # weights = [0.4, 0.3, 0.2, 0.6]  # [smoothness, empty spaces, maximum tile, monotonicity]
    ai = Minimax2048AI(depth=4)
    move = ai.find_best_move(initial_grid)
    print(f"Best move: {move}")