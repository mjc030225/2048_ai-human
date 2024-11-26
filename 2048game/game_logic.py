import random
from prune import Minimax2048AI

class Game2048:
    def __init__(self, mat=None, score=0, mode='human'):
        self.mat = mat if mat is not None else self._initialize_game()
        self.score = score
        self.move_flag = 0
        self.tree = None
        self.wh_move = 1
        self.mode = mode
        # if mode == 'ai':
        self.tree = Minimax2048AI(depth=4)
            # self.load_ai_data()

    def _initialize_game(self):
        # 初始化游戏时在两个随机位置生成数字 2
        mat = [[0] * 4 for _ in range(4)]
        positions = random.sample(range(16), 2)
        for pos in positions:
            i, j = divmod(pos, 4)
            mat[i][j] = 2
        return mat

    def load_ai_data(self):
        mat = self.tree.mat_init(self.mat)
        move = self.tree.find_best_move(mat)
        self.mat, _ = self._process_move(move, self.mat)

    def _generate_random_tile(self,mat):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
        if not empty_positions:
            return
        i, j = random.choice(empty_positions)
        mat[i][j] = random.choices([2, 4], weights=[9, 1])[0]
        return mat
        

    def _get_key(self, command):
        command_list = {'w':'up','s':'down','a':'left', 'd':'right'}
        assert self.mode == 'human', 'make sure that human mode.'
        self.mat , _ = self._process_move(command_list[command] , self.mat) 
        print(self.mat)

    def _merge_line(self, line):
        # 合并非零元素
        line = [num for num in line if num != 0]
        merged = []
        skip = False
        for i in range(len(line)):
            if skip:
                skip = False
                continue
            if i < len(line) - 1 and line[i] == line[i + 1]:
                merged.append(line[i] * 2)
                self.score += line[i] * 2
                skip = True
            else:
                merged.append(line[i])
        # 填充剩余空位
        merged += [0] * (4 - len(merged))
        return merged

    def _process_move(self, key, mat):
        original = [row[:] for row in mat]
        if key == 'left':
            mat = [self._merge_line(row) for row in mat]
        elif key == 'right':
            mat = [self._merge_line(row[::-1])[::-1] for row in mat]
        elif key == 'up':
            mat = self._transpose(mat)
            mat = [self._merge_line(row) for row in mat]
            mat = self._transpose(mat)
        elif key == 'down':
            mat = self._transpose(mat)
            mat = [self._merge_line(row[::-1])[::-1] for row in mat]
            mat = self._transpose(mat)
        self.move_flag = 1 if mat != original else 0
        if self.move_flag:
            mat = self._generate_random_tile(mat)
        return mat, self.move_flag

    def _transpose(self, mat):
        return [[mat[j][i] for j in range(4)] for i in range(4)]

    def is_game_over(self):
        if any(0 in row for row in self.mat):
            return False
        for i in range(4):
            for j in range(4):
                if (i > 0 and self.mat[i][j] == self.mat[i - 1][j]) or \
                   (j > 0 and self.mat[i][j] == self.mat[i][j - 1]):
                    return False
        return True

    def return_data(self):
        mat_display = [[str(cell) if cell != 0 else '' for cell in row] for row in self.mat]
        return {'data': mat_display, 'score': self.score, 'wh_move': 0 if self.is_game_over() else 1}
