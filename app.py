from flask import Flask, request, jsonify, render_template
from tasks import add_task, get_tasks, update_task, delete_task

app = Flask(__name__)

# Главная страница, которая возвращает HTML
@app.route('/')
def index():
    return render_template('index.html')

# POST /tasks - добавление новой задачи
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data or 'priority' not in data:
        return jsonify({'error': 'Title and priority are required'}), 400
    task = add_task(data['title'], data['priority'])
    return jsonify(task.to_dict()), 201

# GET /tasks - получение списка всех задач
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(get_tasks()), 200

# PUT /tasks/<task_id> - обновление задачи
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    data = request.get_json()
    task = update_task(task_id, data.get('title'), data.get('priority'))
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({'error': 'Task not found'}), 404

# DELETE /tasks/<task_id> - удаление задачи
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    task = delete_task(task_id)
    if task:
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
