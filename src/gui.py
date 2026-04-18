# inside project/src folder

import tkinter as tk
from tkinter import ttk, messagebox
from config.config import Config

from src.exp import Exp


class Gui:
    """
    The window has 5 sections:
        - Header bar
        - Top Left: add task name + difficulty
        - Top Right: task list
        - Time row: total time entry and Generate Schedule button
        - Results (bottom): schedule generated using formula
    """

    def __init__(self):
        """
        Tkinter window and sections
        """
        self.exp = Exp(self)

        self.root = None
        self.task_entry = None
        self.difficulty_entry = None
        self.time_entry = None
        self.task_count_label = None
        self.task_list = None
        self.schedule = None

        self.create_window()
        self.create_header()
        self.create_main()
        self.create_time()
        self.create_schedule()

    def create_window(self):
        """
        Creates Tk window (title, size, background, ttk styles).
        """
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(Config.window_width, Config.window_height))
        self.root.title("Time Manager")
        self.root.configure(bg=Config.bg_color)
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure(
            "TButton",
            background=Config.button_color,
            foreground="white",
            font=Config.font_normal,
        )
        style.map("TButton", background=Config)

        style.configure(
            "TLabel",
            background=Config.bg_color,
            foreground=Config.text_color,
            font=Config.font_normal,
        )
        style.configure("TFrame", )


    def create_header(self):
        """
        Header bar with title and labels
        """
        pass

    def create_main(self):
        """
        Creates the two-column layout (left with add assignment, right with task list)
        """
        pass

    def create_left_task(self):
        """
        Left: add assignment name and difficulty entry box --> add task button
        """
        pass

    def create_right_task(self):
        """
        Right: list of added tasks with name and difficulty
        """
        pass

    def create_time_done(self):
        """
        Add total study time entry box --> create schedule button
        """
        pass

    def display_schedule(self):
        """
        Display generated schedule using formulas in exp
        """
        pass

    def add_task_button(self):
        """
        when user clicks add button, read from assignment name and difficulty entry
        """
        pass

    def clear_button(self):
        """
        when user clicks clear button from task list, reset all sections
        """
        pass

    def schedule_button(self):
        """
        when user clicks generate schedule button, read from total time and use exp formulas
        """
        pass

    def update_task_count(self):
        """
        Update the task count label in task list section
        """
        pass
