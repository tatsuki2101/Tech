const API_URL = 'http://127.0.0.1:5000/tasks';

// タスク一覧を表示
async function renderTasks() {
    const res = await fetch(API_URL);
    const tasks = await res.json();
    const taskList = document.getElementById('task-list'); // タスクリストの表示部分を取得
    taskList.innerHTML = ''; // 一旦、リストを空にする

    tasks.forEach(task => {
        const li = document.createElement('li'); // 新しいリスト項目を作る
        li.innerHTML = `
            <span>${task.title}</span>
            <button onclick="deleteTask(${task.id})">削除</button>
        `;
        taskList.appendChild(li); // 作ったリスト項目を表示部分に追加
    });
}

// 新しいタスクを追加
document.getElementById('add-task').addEventListener('click', async () => {
    const title = document.getElementById('new-task').value.trim(); // 入力されたタスクを取得
    if (!title) return; // タスクが空白なら何もしない
    // タスクを追加
    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title }),
    });
    document.getElementById('new-task').value = ''; // 入力欄をクリア
    renderTasks(); // リストを再描画
});

// タスクを削除
async function deleteTask(id) {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
    renderTasks(); // リストを再描画
}

// 初期化
renderTasks();