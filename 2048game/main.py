from flask import Flask, render_template, jsonify, request
from game_logic import Game2048  # 假设 `Game2048` 类在独立的 `game_logic.py` 中
import uuid  # 用于生成唯一的 game_id

# 创建 Flask 应用
app = Flask(__name__, template_folder='./templates', static_folder='./templates')

# 初始化游戏状态存储
games = {}

# 创建新游戏或重置游戏
@app.route('/submit', methods=['POST'])
def submit():
    command = request.form.get('command', type=str)
    game_id = request.form.get('game_id')  # 检查是否有现有游戏 ID

    if command == 'reset':
        game_id = str(uuid.uuid4())
        games[game_id] = Game2048()
    else:
        return jsonify({'error': 'Invalid command'}), 400

    # 返回游戏状态
    data = games[game_id].return_data()
    return jsonify({'game_id': game_id, **data})

# AI 模式自动执行
@app.route('/ai-mode', methods=['POST'])
def auto_ai():
    req_data = request.get_json()
    game_id = req_data.get('game_id')

    if not game_id or game_id not in games:
        return jsonify({'error': 'Invalid game ID'}), 404

    game = games[game_id]
    game.load_ai_data()
    return jsonify(game.return_data())

# 用户移动
@app.route('/move', methods=['POST'])
def upload():
    req_data = request.get_json()
    game_id = req_data.get('game_id')
    command = req_data.get('command')
    if not command or command not in ['w', 'a', 's', 'd']:
        return jsonify({'error': 'Invalid command'}), 400

    if not game_id or game_id not in games:
        return jsonify({'error': 'Invalid game ID'}), 404

    game = games[game_id]
    game._get_key(command)
    return jsonify(game.return_data())

# 默认页面
@app.route('/', methods=['GET'])
def set_web():
    # 创建新游戏并生成唯一的 game_id
    game_id = str(uuid.uuid4())
    games[game_id] = Game2048()
    data = games[game_id].return_data()
    return render_template('index.html', game_id=game_id, data=data['data'], score=data['score'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7892, debug=True)