# time-manager

## **Sales Pitch**:
> Have you ever felt like you spend hours doing one task, but it doesn't feel like much progress was made? You sit in front of your computer slaving away at homework after homework but never truly finish anything until the last minute? Have the stress of deadlines only kicked in the night before, leaving you frantically working to submit sub-par assignments?  

> Look no further than the Time Manager, a simple and easy-to-use program to schedule your time that way you finish all your assignments in a timely manner! 


## **Overview**:
- My final project will be a time manager to help figure out how much time to spend on assignments, while scheduling in breaks. Similar to the Pomodoro technique, my project will calculate how much time to spend on certain assignments given their difficulty while considering how much time is available to work. The amount of time given for each break and when each break is given will be calculated with an equation I will create. The project will take in:
- one or more **assignment names** (e.g. `"BCOG200 HW1"`, `"MSE404 Lab Report"`)
- a **difficulty rating** for each assignment, from 1 (easy) to 5 (hard)
- the total **uninterrupted study time** they have available, in minutes

The program then splits the available time into study blocks and break blocks, giving harder assignments proportionally more study (and break) time than easier ones. The full schedule is displayed.

## **Functions**:
- __init__(self gui)
- add_tasks(self, task_name, task_difficulty)
- run_program(self, total_time)
- clear(self)
- calculate_breaks(self, tasks, total_time): 80% of the total time goes to **studying**, 20% goes to **breaks**.

## **Use Case**:
- Designed for students who want to make the most of a finite block of study time and want a clear, fair allocation across competing assignments without doing the math themselves.


## **File Structure**:

```
time-manager/
├── README.md
├── run_experiment.py          # entry point, launches the GUI
├── config/
│   └── config.py              # window size, colors, fonts
├── src/
│   ├── exp.py                 # Exp class: task storage + scheduling logic
│   └── gui.py                 # Gui class: tkinter window + event handlers
└── tests/
    └── test_exp.py            # unit tests for the Exp class
    └── testing_procedure.txt  # testing procedure (written out)
```

## **Installation**:
The project uses only the **Python standard library** (`tkinter`,`math`). There are no external dependencies to install, so there is no `requirements.txt`.

## **How to Run**:
After cloning the github, navigate to the time-manager folder holding the run_experiment.py file. Run the file using 
> python run_experiment.py

A window titled "Time Manager" will open. To use it:

1. In the **Add Assignment** box on the left, type an assignment name.
2. Pick a difficulty from 1 to 5 using the buttons.
3. Click **Add Task** or press Enter. The task appears in the **Task
   List** on the right.
4. Repeat for as many assignments as you want to schedule.
5. In the **Total Study Time** row, enter how many minutes you have
   available, then click **Generate Schedule**.
6. The generated schedule appears at the bottom, showing study time,
   break time, and a difficulty bar for each assignment.

Use **Clear All** to reset everything and start over.

## **Project timeline**:
- Week 8-9: build class and function headers, write documentation for each function
- Week 10-12: code at least 3 functions, include more if needed
- Week 13-15: finalize code, improve user interface

