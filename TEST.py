class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, "status": "не выполнено"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполнено"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена")

    def  show_tasks(self):
        print("текущие задачи")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task("01.06.2024","Прочитать книгу")
t.add_task("06.06.2024","Полететь в Турцию")
t.add_task("07.06.2024","Поучиться писать программу")

t.show_tasks()

t.complete_tasks("Полететь в Турцию")
t.show_tasks()
