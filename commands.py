class TodoList:
    def __init__(self):
        self.tasks = {}
"""Adding tasks -- users add new tasks to the to-do list"""
def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = {"tasks": task, "complete": False}
  
"""Deleting tasks -- users delete tasks from the to-do list"""
def update_tasks(self):
        new_tasks = {}
        new_number = 1
        for number in sorted(self.tasks.keys()):
            new_tasks[new_number] = self.tasks[number]
            new_number += 1
        self.tasks = new_tasks
  
  def delete_task(self, task_number):
        if task_number in self.tasks:
            del self.tasks[task_number]
            self.update_tasks()
        else:
            print("Task not found!")

"""Marking tasks as completed -- users complete tasks and cross them off"""
def complete_task(self, task_number):
        if task_number in self.tasks:
            self.tasks[task_number]["complete"] = True
        else:
            print("Task not found!")
          
def uncomplete_task(self, task_number):
        if task_number in self.tasks:
            self.tasks[task_number]["complete"] = False
        else:
            print("Task not found!")

"""Viewing tasks -- viewing area for tasks"""
def view_tasks(self):
        print("To Do List:")
        for number, task in self.tasks.items():
            if task["complete"]:
                status = "Complete"
            else:
                status = "Incomplete"
            print(str(number) + ". " + task["tasks"] + " [" + status + "]")

"""Editing tasks -- users edit existing tasks"""
