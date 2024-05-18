# Создаем Task manager.
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Должны быть функции для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = "Not completed"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if index < len(self.tasks):
            self.tasks[index].status = "Completed"
        else:
            print("Invalid task index")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "Not completed"]
        if len(current_tasks) == 0:
            print("No current tasks")
        else:
            for index, task in enumerate(current_tasks):
                print(f"{index+1}. {task.description} - Deadline: {task.deadline}")