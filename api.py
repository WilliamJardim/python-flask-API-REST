from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados para a API
tasks = [
    {
        'id': 1,
        'title': 'Aprender Flask',
        'done': False
    },
    {
        'id': 2,
        'title': 'Criar uma API REST',
        'done': False
    }
]

# Endpoint para retornar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Endpoint para retornar uma tarefa específica com base no ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    return jsonify({'task': task})

# Endpoint para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()  # Obtém o JSON enviado
    task = {
        'id': len(tasks) + 1,
        'title': new_task['title'],
        'done': new_task.get('done', False)
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Endpoint para atualizar o status de uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    return jsonify({'task': task})

# Endpoint para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Tarefa deletada'}), 200

if __name__ == '__main__':
    app.run(debug=True)