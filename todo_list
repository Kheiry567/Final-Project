"""
Our project is a To-Do list which allows a user to assign tasks for them to complete throughout the day.
It allows for adding, updating and deleting tasks. In addition, a user can utilize a spinbox timer to decide what hour of the day to complete said tasks.
Our To-Do list program also logs how many days a user has completed every task they have assigned for themselves per day.
In order to run this program from the command line, a user can simply input: python todo_list.py
"""
import tkinter 
from tkinter import ttk
from tkinter import messagebox

class PersonalToDoList:
    """
    A class for creating an instance of a To-Do list
    
    Attributes:
        window (gui): creates a window for users to operate the To-Do list 
    """
    def __init__(self, window):
        """
        Initializes a PersonalToDoList object
        
        Args:
            window (gui): see class documentation
        """
        self.window = window
        self.window.title("Personal To-Do List")
        self.total_days = 0
        self.task_rows = []
        self.create_widgets()

    def create_widgets(self):
        """
        Add widgets for user interaction
        """
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()

        self.create_consistency_check_widgets()

        self.user_frame = tkinter.LabelFrame(self.frame, text="Tasks")
        self.user_frame.grid(row=0, column=0, padx=30, pady=30)
        
        self.create_task_row(0)

        self.add_task_button = tkinter.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.create_log_button()

    def create_task_row(self, index):
        """
        Creates a task row for users to manipulate the interface
        
        Args:
            index (gui): determines the row assignment for a task
        """
        task_encourage = tkinter.Label(self.user_frame, text="Get these done!")
        task_encourage.grid(row=0, column=1)
        task_label = tkinter.Label(self.user_frame, text=f"Task {index+1}")
        task_label.grid(row=index+1, column=0)

        entry = tkinter.Entry(self.user_frame)
        entry.grid(row=index+1, column=1)

        title = tkinter.Label(self.user_frame, text="Is This Task Complete?")
        title.grid(row=0, column=2)
        title_combobox = ttk.Combobox(self.user_frame, values=["Complete", "Incomplete"])
        title_combobox.grid(row=index+1, column=2)

        start_label = tkinter.Label(self.user_frame, text="Start Time")
        start_label.grid(row=0, column=3)
        start_spinbox = tkinter.Spinbox(self.user_frame, from_="0", to="24")
        start_spinbox.grid(row=index+1, column=3)

        delete_button = tkinter.Button(self.user_frame, text="Delete Task", command=lambda i=index: self.delete_task(i))
        delete_button.grid(row=index+1, column=4)

        self.task_rows.append((task_label, entry, title_combobox, start_spinbox, delete_button))

    def create_consistency_check_widgets(self):
        """
        Adds widgets for users to document whether or not they have completed every task they had assigned themselves for the day
        """
        self.days_frame = tkinter.LabelFrame(self.frame)
        self.days_frame.grid(row=1, column=0, padx=30, pady=30)

        self.daycheck_label = tkinter.Label(self.days_frame, text="Did you complete all your tasks today?")
        self.checkyes_var = tkinter.StringVar(value="No")
        self.daycheck_yes = tkinter.Checkbutton(self.days_frame, text="I did!", variable=self.checkyes_var, onvalue="Yes", offvalue="No")
        self.daycheck_label.grid(row=0, column=0)
        self.daycheck_yes.grid(row=1, column=0)

    def create_log_button(self):
        """
        Creates a button in order to log what tasks have been completed for the day
        """
        self.button = tkinter.Button(self.frame, text="Log Today's Tasks", command=self.log_today)
        self.button.grid(row=2, column=1, padx=30, pady=30)

    def log_today(self):
        """
        Checks if every task assigned for the day has been completed, and if so, logs that day
        """
        daycheck_label = self.checkyes_var.get()
        print(f"Did you complete all of your tasks today? {daycheck_label}")
        if daycheck_label == "Yes":
            self.total_days += 1
        print(f"You completed every task per day for {self.total_days} days.")

    def add_task(self):
        """
        Allows a user to add another task row
        """
        index = len(self.task_rows)
        self.create_task_row(index)

    def delete_task(self, index):
        """
        Allows a user to delete a task they have previously assigned for themselves
        
        Args:
            index (gui): determines the row assignment for a task
        """
        row = self.task_rows.pop(index)
        for widget in row:
            widget.destroy()

if __name__ == "__main__":
    window = tkinter.Tk()
    app = PersonalToDoList(window)
    window.mainloop()
