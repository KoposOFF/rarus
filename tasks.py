from models import Task

tasks = {}  # словарь для хранения задач с уникальными ID
current_id = 1  # переменная для генерации уникальных ID

def add_task(title, priority):
    """
    Добавление новой задачи. ID генерируется автоматически.
    """
    global current_id
    task = Task(title, priority)
    task.id = current_id  # присваиваем уникальный ID
    tasks[current_id] = task  # добавляем задачу в словарь
    current_id += 1  # увеличиваем ID для следующей задачи
    return task

def get_tasks():
    """
    Получение всех задач в виде списка.
    """
    return [task.to_dict() for task in tasks.values()]

def get_task(task_id):
    """
    Получение конкретной задачи по ID.
    """
    return tasks.get(task_id)

def update_task(task_id, title, priority):
    """
    Обновление задачи по ID.
    """
    task = tasks.get(task_id)
    if task:
        task.title = title
        task.priority = priority
        return task
    return None

def delete_task(task_id):
    """
    Удаление задачи по ID.
    """
    return tasks.pop(task_id, None)
