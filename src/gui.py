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
        self.create_time_done()
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
            foreground="#a8c4f0",
            font=Config.font_normal,
        )
        style.map(
            "TButton",
            background=[("active", Config.button_color)],
            foreground=[("active", "#2c3e6b")],
        )

        style.configure(
            "TLabel",
            background=Config.bg_color,
            foreground=Config.text_color,
            font=Config.font_normal,
        )
        style.configure(
            "TFrame",
        )

    def create_header(self):
        """
        Header bar with title and labels
        """
        header = tk.Frame(self.root, bg=Config.header_color, height=60)
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text=" * TIME MANAGER * ",
            font=Config.font_title,
            bg=Config.header_color,
            fg="white",
        )
        title.pack(side=tk.LEFT, padx=20, pady=10)

        subtitle = tk.Label(
            header,
            text="Schedule your study time!",
            font=Config.font_small,
            bg=Config.header_color,
            fg="white",
        )
        subtitle.pack(side=tk.LEFT, padx=5, pady=10)

    def create_main(self):
        """
        Creates the two-column layout (left with add assignment, right with task list)
        """
        main_window = tk.Frame(self.root, bg=Config.bg_color, height=300)
        main_window.pack(fill=tk.X, padx=20, pady=15)
        main_window.pack_propagate(False)

        main_window.columnconfigure(0, weight=1)
        main_window.columnconfigure(1, weight=1)
        main_window.rowconfigure(0, weight=1)

        left_window = tk.Frame(main_window, bg=Config.bg_color)
        left_window.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        right_window = tk.Frame(main_window, bg=Config.bg_color)
        right_window.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        self.create_left_task(left_window)
        self.create_right_task(right_window)

    def create_left_task(self, parent=None):
        """
        Left: add assignment name and difficulty entry box --> add task button
        """
        if parent is None:
            parent = self.root

        section = tk.LabelFrame(
            parent,
            text=" * Add Assignment * ",
            font=Config.font_bold,
            bg=Config.bg_color,
            fg="#2c3e6b",
            padx=15,
            pady=10,
        )
        section.pack(fill=tk.BOTH, expand=True, ipady=4)

        # assignment
        tk.Label(
            section,
            text="Assignment Name:",
            bg=Config.bg_color,
            fg=Config.text_color,
            font=Config.font_normal,
        ).pack(anchor=tk.W, pady=(5, 2))
        self.name_entry = ttk.Entry(section, width=35)
        self.name_entry.pack(fill=tk.X, pady=(0, 10))

        # diff score
        tk.Label(
            section,
            text="Difficulty (1 = easy  →  5 = hard):",
            bg=Config.bg_color,
            fg=Config.text_color,
            font=Config.font_normal,
        ).pack(anchor=tk.W, pady=(0, 2))

        diff_frame = tk.Frame(section, bg=Config.bg_color)
        diff_frame.pack(fill=tk.X, pady=(0, 12))

        self.difficulty_var = tk.IntVar(value=3)

        for d in range(1, 6):
            rb = tk.Radiobutton(
                diff_frame,
                text=str(d),
                variable=self.difficulty_var,
                value=d,
                bg=Config.bg_color,
                fg=Config.text_color,
                selectcolor="blue",
                font=Config.font_normal,
                activebackground=Config.bg_color,
            )
            rb.pack(side=tk.LEFT, padx=6)

        # buttons
        add_btn = ttk.Button(section, text="➕  Add Task", command=self.add_task_button)
        add_btn.pack(fill=tk.X, pady=(4, 0))

        # testing enter key https://www.geeksforgeeks.org/python/how-to-bind-the-enter-key-to-a-tkinter-window/
        self.name_entry.bind("<Return>", lambda e: self.add_task_button())

    def create_right_task(self, parent=None):
        """
        Right: list of added tasks with name and difficulty
        """
        if parent is None:
            parent = self.root

        section = tk.LabelFrame(
            parent,
            text=" * Task List * ",
            font=Config.font_bold,
            bg=Config.bg_color,
            fg="#2c3e6b",
        )
        section.pack(fill=tk.BOTH, expand=True)

        # count
        self.task_count_label = tk.Label(
            section,
            text="Tasks added: 0",
            bg=Config.bg_color,
            fg=Config.text_color,
            font=Config.font_small,
        )
        self.task_count_label.pack(anchor=tk.W, pady=(0, 5))

        # all assignments
        list_frame = tk.Frame(section, bg=Config.bg_color)
        list_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=Config.font_small,
            bg="#f9f9f9",
            fg=Config.text_color,
            selectbackground="#3a5fc8",
            selectforeground="white",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightcolor="#3a5fc8",
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        # clear button
        clear_btn = ttk.Button(section, text="🗑  Clear All", command=self.clear_button)
        clear_btn.pack(fill=tk.X, pady=(8, 0))

    def create_time_done(self):
        """
        Add total study time entry box --> create schedule button
        """
        time_frame = tk.Frame(self.root, bg=Config.bg_color)
        time_frame.pack(fill=tk.X, padx=20, pady=(0, 10))

        section = tk.LabelFrame(
            time_frame,
            text=" * Total Study Time * ",
            font=Config.font_bold,
            bg=Config.bg_color,
            fg="#2c3e6b",
        )
        section.pack(fill=tk.X)

        row = tk.Frame(section, bg=Config.bg_color)
        row.pack(fill=tk.X)

        tk.Label(
            row,
            text="Available minutes:",
            bg=Config.bg_color,
            fg=Config.text_color,
            font=Config.font_normal,
        ).pack(side=tk.LEFT, padx=(0, 10))

        self.time_entry = ttk.Entry(row, width=10)
        self.time_entry.pack(side=tk.LEFT, padx=(0, 20))
        self.time_entry.bind("<Return>", lambda e: self.schedule_button())

        gen_btn = ttk.Button(
            row, text="📅  Generate Schedule", command=self.schedule_button
        )
        gen_btn.pack(side=tk.LEFT)

    def create_schedule(self):
        """
        Create schedule area
        """
        self.results_frame = tk.LabelFrame(
            self.root,
            text=" * Schedule * ",
            font=Config.font_bold,
            bg=Config.bg_color,
            fg="#2c3e6b",
        )
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))

        scrollbar = tk.Scrollbar(self.results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results_text = tk.Text(
            self.results_frame,
            yscrollcommand=scrollbar.set,
            font=("Courier", 13),
            bg="#f0f4f8",
            fg=Config.text_color,
            relief=tk.FLAT,
            wrap=tk.WORD,
            padx=10,
            pady=8,
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.results_text.yview)

        # default text
        self._set_text("Your schedule will appear here after you add tasks.")

    def display_schedule(self, schedule):
        """
        Display generated schedule using formulas
        """
        lines = ["═" * 60]
        lines.append(f"{'ASSIGNMENT':<28} {'STUDY':>10} {'BREAK':>10}  DIFF")
        lines.append("─" * 60)

        total_study = 0
        total_break = 0
        for item in schedule:
            name = item["assignment"]
            if len(name) > 26:
                name = name[:24] + ".."
            study = item["study_time"]
            break_time = item["break_time"]
            diff = item["difficulty"]
            total_study += study
            total_break += break_time
            visual = "█" * diff + "░" * (5 - diff)
            lines.append(f"{name:<28} {study:>6} min {break_time:>6} min  {visual}")

        lines.append("─" * 60)
        lines.append(f"{'TOTALS':<28} {total_study:>6} min {total_break:>6} min")
        lines.append("═" * 60)
        lines.append("")

        self._set_text("\n".join(lines))

    def add_task_button(self):
        """
        when user clicks add button, read from assignment name and difficulty entry
        """
        name = self.name_entry.get()
        difficulty = self.difficulty_var.get()

        error = self.exp.add_task(name, difficulty)
        if error:
            messagebox.showerror("Invalid Input", error)
            return

        stars = "★" * difficulty + "☆" * (5 - difficulty)
        self.task_listbox.insert(tk.END, f"  {name}  [{stars}]  diff {difficulty}")

        self.update_task_count()

        self.name_entry.delete(0, tk.END)
        self.difficulty_var.set(3)
        self.name_entry.focus()

    def clear_button(self):
        """
        when user clicks clear button from task list, reset all sections
        """
        self.exp.clear()
        self.task_listbox.delete(0, tk.END)
        self.update_task_count()
        self.time_entry.delete(0, tk.END)
        self._set_text("Your schedule will appear here after you add tasks.")

    def schedule_button(self):
        """
        when user clicks generate schedule button, read from total time and use exp formulas
        """
        time = self.time_entry.get().strip()
        try:
            total_time = int(time)
        except ValueError:
            messagebox.showerror("Invalid Input", "Total time must be a whole number.")
            return

        result = self.exp.run(total_time)

        if isinstance(result, str):
            messagebox.showerror("Error", result)
            return

        self.display_schedule(result)

    def update_task_count(self):
        """
        Update the task count label in task list section
        """
        count = self.exp.get_task_count()
        noun = "task" if count == 1 else "tasks"
        self.task_count_label.config(text=f"Tasks added: {count} {noun}")

    def _set_text(self, text):
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, text)
        self.results_text.config(state=tk.DISABLED)
