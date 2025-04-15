import pytest
import json
from app import app, db, Task

@pytest.fixture
def client():
    """
    テスト時だけ In-Memory DB を使う設定にし、
    毎回のテストでテーブルを作り直すためのフィクスチャ。
    """
    # テスト用設定
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # インメモリDB

    # 空の状態にする
    with app.app_context():
        db.drop_all()
        db.create_all()

    # テストクライアント生成
    with app.test_client() as client:
        yield client

def test_get_tasks_empty(client):
    """
    タスクがまだない状態で /tasks に GET リクエストを送り、
    空のリストが返却されることを確認する。
    """
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_create_task(client):
    """
    新しいタスクを作成し、201ステータスが返却されることを確認。
    また、その後 /tasks に GET した際に作成したタスクが含まれていることを確認。
    """
    # 新規タスク作成
    response = client.post('/tasks',
                           data=json.dumps({'title': 'Test Task 1'}),
                           content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Task created successfully'

    # 作成後の一覧を取得
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks = response.get_json()
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Test Task 1'
    assert tasks[0]['completed'] is False

def test_update_task(client):
    """
    既存のタスクを更新し、200ステータスが返却されることを確認。
    また、更新が正しく反映されているかを確認。
    """
    # テスト用タスクを先に作成
    response = client.post('/tasks',
                           data=json.dumps({'title': 'Update Task'}),
                           content_type='application/json')
    assert response.status_code == 201

    # タスクIDを取得
    created_task_id = Task.query.first().id

    # タスクを更新
    response = client.put(f'/tasks/{created_task_id}',
                          data=json.dumps({'title': 'Updated Title', 'completed': True}),
                          content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Task updated successfully'

    # 更新後の内容を確認
    with app.app_context():
        updated_task = db.session.get(Task, created_task_id)
        assert updated_task.title == 'Updated Title'
        assert updated_task.completed is True

# テストケース：タスクの削除（課題で作成）