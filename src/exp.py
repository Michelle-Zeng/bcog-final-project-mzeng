# inside project/src folder

import math
from config.config import Config


class Exp:
    def __init__(self, the_gui):
        self.gui = the_gui
        self.tasks = {}

    def add_task(self, name, difficulty):
        """
        Description: Stores single task into task dictionary.
        Parameters:
            name (str): assignment name, non-empty
            difficulty (int): ranking from 1 (easy) to 5 (hard)
        Returns:
            str: empty str if valid add, error message if invalid add
        """
        name = name.strip()
        if not name:
            return "Task name cannot be empty"
        if name in self.tasks:
            return 'Task names "{name}" already exists'
        if not isinstance(difficulty, int) or not (1 <= difficulty <= 5):
            return "Difficulty must be an integer between 1 and 5"
        self.tasks[name] = difficulty
        return ""

    def run(self, total_time):
        """
        Description: Checks total_time and calls calculate_breaks to produce a schedule.
        Parameters:
            total_time (int): total uninterrupted minutes available
        Returns:
            schedule (list of dict): the calculated schedule
        """
        if not self.tasks:
            return "No tasks added: please add at least one"
        if not isinstance(total_time, int) or not (0 < total_time):
            return "Total time must be an integer greater than 0"

        return self.calculate_breaks(self.tasks, total_time)

    def clear(self):
        """
        Description: Resets task dictionary and total_time to default.
        Parameters: none
        Returns: none
        """
        self.tasks = {}

    def calculate_breaks(self, tasks, total_time):
        """
        Description: Calculates study and break time for each assignment.
        Parameters:
            tasks (dict): names mapped to difficulty
            total_time (int): total minutes available
        Returns:
            list of dict: each dict contains:
                "assignment" (str), "difficulty" (int),
                "study_time" (float), "break_time" (float)
        """
        """
        Formuals used to calculate time:
            total_time_needed = sum of (difficulty * 10) for all tasks
            factor            = total_time_needed / total_time
            study_time        = difficulty * 10 / factor
            break_time        = (5 + difficulty) / factor
        """
        total_time_needed = sum(d * 10 for d in tasks.values())
        factor = total_time_needed / total_time

        schedule = []
        for name, difficulty in tasks.items():
            study_time = math.ceil((difficulty * 10) / factor)
            break_time = math.ceil((difficulty + 5) / factor)
            schedule.append({
                    "assignment": name,
                    "difficulty": difficulty,
                    "study_time": study_time,
                    "break_time": break_time,
            })

        return schedule

    def get_task_count(self):
        return len(self.tasks)
    
    def get_tasks(self):
        return dict(self.tasks)
    
    def remove_tasks(self, name):
        name = name.strip()
        if name not in self.tasks:
            return 'Task "{name}" not found'
        del self.tasks(name)


# if possible:
# class ChoreManager(Exp):
#     Child class that inherits from Exp
#     Adapts study time management for chores
#     Inherits add_task, run, clear, calculate_breaks
