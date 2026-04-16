# time-manager

## **Sales Pitch**:
> Have you ever felt like you spend hours doing one task, but it doesn't feel like much progress was made? You sit in front of your computer slaving away at homework after homework but never truly finish anything until the last minute? Have the stress of deadlines only kicked in the night before, leaving you frantically working to submit sub-par assignments?  

> Look no further than the Time Manager, a simple and easy-to-use program to schedule your time that way you finish all your assignments in a timely manner! 


## **Overview**:
- My final project will be a time manager to help figure out how much time to spend on assignments, while scheduling in breaks. Similar to the Pomodoro technique, my project will calculate how much time to spend on certain assignments given their difficulty while considering how much time is available to work. The amount of time given for each break and when each break is given will be calculated with an equation I will create. The project will take in assignment names ("BCOG200 homework 1" or "MSE404 Lab Report"), estimated difficulty (from 1-5), and amount of uninterrupted study time available to finish given assignments in minutes as user inputs.

If time permits, I will use the previously described project as a parent class and build a child class for chore time management that inherits the functions/variables.   
TESTING


## **Functions**:
- __init__(self gui)
- add_tasks(self, task_name, task_difficulty)
- run_program(self, total_time)
- clear(self)
- calculate_breaks(self, tasks, total_time): Ex. Time for assignment = difficulty ranking * 10 * factor, Break after assignment = (5 + difficulty ranking) * factor, Factor = (total time needed)/(total time allowed)


## **Use Case**:
- for students who want to schedule their short amount of study time to get the optimal ratio of work and break.


## **Inputs**:
- task name: string
- task difficulty: int
- total study time: int


## **Project timeline**:
- Week 8-9: build class and function headers, write documentation for each function
- Week 10-12: code at least 3 functions, include more if needed
- Week 13-15: finalize code, improve user interface
