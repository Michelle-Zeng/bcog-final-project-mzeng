# inside project/src folder

class Exp:
    def __init__(self, the_gui):
        self.gui = the_gui

    def add_task(self, name, difficulty):
        """
        Description: Stores single task into task dictionary.
        Parameters:
            name (str): assignment name, non-empty
            difficulty (int): ranking from 1 (easy) to 5 (hard)
        Returns:
            str: empty str if valid add, error message if invalid add
        """
        pass
      

    def run(self, total_time):
        """
        Description: Checks total_time and calls calculate_breaks to produce a schedule.
        Parameters:
            total_time (int): total uninterrupted minutes available
        Returns:
            schedule (list of dict): the calculated schedule
            
        """
        pass
      

    def clear(self):
        """
        Description: Resets task dictionary and total_time to default.
        Parameters: none
        Returns: none
        """
        pass
      

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
        pass


# if possible:
# class ChoreManager(Exp):
#     Child class that inherits from Exp
#     Adapts study time management for chores
#     Inherits add_task, run, clear, calculate_breaks

