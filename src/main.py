"""Простой консольный менеджер задач."""
# Title: Task Manager Pro v2.0 (Feature Edition)
tasks = []


def add_task(title):
    """Добавляет задачу в список."""
    task_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": task_id, "title": title, "done": False}
    tasks.append(task)
    return task


def list_tasks():
    """Возвращает список всех задач."""
    return tasks


def complete_task(task_id):
    """Отмечает задачу выполненной. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def delete_task(task_id):
    """Удаляет задачу по номеру. Возвращает True, если задача найдена."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def main():
    """Демонстрация работы менеджера задач."""
    add_task("Выучить Git")
    add_task("Сделать лабораторную работу")
    complete_task(1)
    for task in list_tasks():
        status = "x" if task["done"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")


if __name__ == "__main__":
    main()
