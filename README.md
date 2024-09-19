# ToDo List API

Этот проект представляет собой простое REST API для управления списком задач (ToDo List) с использованием Flask.

## Функциональность API

- **POST /tasks** — добавление новой задачи
- **GET /tasks** — получение списка всех задач
- **PUT /tasks/<task_id>** — обновление задачи по её ID
- **DELETE /tasks/<task_id>** — удаление задачи по её ID

## Стек технологий

- Python
- Flask

## Установка и запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/KoposOFF/rarus.git
cd todo
python -m venv venv (для linux/mac : python3 -m venv venv)
Активируйте виртуальное окружение:
venv\Scripts\activate (для linux/mac : source venv/bin/activate )
Установка зависимостей:
pip install -r requirements.txt
запуск основного файла 
python app.py
```
Простой веб-интерфейс доступен по адресу http://127.0.0.1:5000



