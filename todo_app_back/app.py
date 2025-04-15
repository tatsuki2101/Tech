import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)  # フロントエンドとの通信を許可

# モデル定義
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# データベースの初期化（既存のファイルがない場合のみ作成）
if not app.config.get('TESTING', False):
    if not os.path.exists('db.sqlite3'):
        with app.app_context():
            db.create_all()

# タスク一覧を取得
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in tasks])

# 新しいタスクを作成
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

# タスクを更新
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

# タスクを削除
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)