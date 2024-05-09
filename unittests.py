"""Unit Tests for the application"""
import tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Spinbox
from tkinter import Entry
from tkinter import Label

from todo_list import PersonalToDoList

def test_add_task():
    window = tkinter.Tk()
    task = PersonalToDoList(window)
    initial_task_count = len(task.task_rows)
    task.add_task()
    assert len(task.task_rows) == initial_task_count + 1
    new_task_index = initial_task_count
    new_task_row = task.task_rows[new_task_index]
    assert isinstance(new_task_row[0], Label)
    assert isinstance(new_task_row[1], Entry)
    assert isinstance(new_task_row[2], ttk.Combobox)
    assert isinstance(new_task_row[3], Spinbox)
    assert isinstance(new_task_row[4], tkinter.Button)
    window.destroy()

def test_delete_task():
    window = tkinter.Tk()
    task = PersonalToDoList(window)
    task.add_task()
    initial_task_count = len(task.task_rows)
    task.delete_task(initial_task_count - 1)
    assert len(task.task_rows) == initial_task_count - 1
    window.destroy()

def test_log_today():
    window = tkinter.Tk()
    task = PersonalToDoList(window)
    task.checkyes_var.set("Yes")
    task.log_today()
    assert task.total_days == 1
    window.destroy()

def test_boundary_test():
    window = tkinter.Tk()
    task = PersonalToDoList(window)
    for i in range(10):
        task.add_task()
    task.add_task()
    assert len(task.task_rows) == 10
    window.destroy()

def test_start_time_input():
    window = tkinter.Tk()
    task = PersonalToDoList(window)
    task.task_rows[0][3].delete(0, 'end')
    task.task_rows[0][3].insert(0, '12')
    assert task.task_rows[0][3].get() == '12'
    task.task_rows[0][3].delete(0, 'end')
    task.task_rows[0][3].insert(0, '25')
    assert task.task_rows[0][3].get() != '25'
    window.destroy()

if __name__ == '__main__':
    test_add_task()
    test_delete_task()
    test_log_today()
    test_boundary_test()
    test_start_time_input()
    print("All tests passed!")
