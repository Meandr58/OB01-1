from datetime import datetime

class Task:
    def __init__(self, description=None, deadline=None):
        self.description = description
        self.deadline = deadline
        self.is_completed = False
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def mark_as_completed(self):
        self.is_completed = True

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Неверный индекс задачи")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def __str__(self):
        if self.description is None:
            pending_tasks = self.get_pending_tasks()
            return "\n".join(str(task) for task in pending_tasks)

        else:
            deadline_str = self.deadline.date() if self.deadline else "Без срока"
            return f"Задача: {self.description}, Срок: {deadline_str}"


task_manager = Task()
task_manager.add_task("Купить билет в кино", datetime(2023, 6, 21))
task_manager.add_task("Сделать домашнее задание", datetime(2023, 6, 20))
task_manager.add_task("Сдать в чистку куртку", datetime(2023, 6, 22))
task_manager.add_task("Позвонить родителям", datetime(2023, 6, 19))
task_manager.add_task("Заплатить за коммуналку", datetime(2023, 6, 22))
print(task_manager)

task_manager.mark_task_as_completed(3)
task_manager.mark_task_as_completed(0)
task_manager.mark_task_as_completed(1)

print(task_manager)

task_manager.mark_task_as_completed(0)

print("\nАктуальный перечень невыполненных задач:")
print(task_manager)
