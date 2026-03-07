# bcog-final-project-mzeng
Final project for bcog200

1. My final project will be a time manager to help figure out how much time to spend on assignments, while scheduling in breaks. Similar to the Pomodoro technique, my project will calculate how much time to spend on certain assignments given their difficulty while considering how much time is available to work. The amount of time given for each break and when each break is given will be calculated with an equation I will create. The project will take in assignment names ("BCOG200 homework 1" or "MSE404 Lab Report"), estimated difficulty (from 1-5), and amount of uninterrupted study time available to finish given assignments in minutes as user inputs.

If time permits, I will use the previously described project as a parent class and build a child class for chore time management that inherits the functions/variables.

2. functions

a. **add_tasks** will take in user input (assignment name, diffculty ranking) and store the values in a dictionary

b. **calculate_time** will take in user input (amount of time to work) and store to global variable

c. **calculate_breaks** will take in the created dictionary and total time variable to calculate breaks
Ex. Time for assignment = difficulty ranking * 10 * factor, Break after assignment = (5 + difficulty ranking) * factor, Factor = (total time needed)/(total time allowed)

3. Individual projcet, Michelle Zeng, Github = Michelle-Zeng

4. Project timeline:
Week 8-9: build class and function headers, write documentation for each function
Week 10-12: code at least 3 functions, include more if needed
Week 13-15: finalize code, improve user interface
