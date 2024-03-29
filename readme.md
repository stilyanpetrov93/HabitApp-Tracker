# My HabitApp Tracker

This HabitApp Tracker is backend CLI in Python providing a user to record, analyse, complete and delete habits. The CLI stores
the data in sqlite3 tables so the user can retrieve a data for analysis. This Tracker
is perfect tool to overcome bad habits or creating new good ones. 

# Requirements
To use the HabitApp Tracker, you will need to install Python 3.8 or later and the following tools:
- pip install questionary
- pip install freezegun
 
# Installation 
To use this HabitApp tracker you will need to install Python and the below-mentioned tools. Requirements file will be
included in the repository and needs to be downloaded along with the rest of the project.
- pip install -r requirements.txt

# Usage
Run the following command to start the HabitApp tracker:
- python main.py

# CLI Interface
The CLI interface allows the user the run the following actions:
- Add a habit
- Remove a habit
- Complete a habit
- Search for a habit by name
- Display all habits 
- Display Habits Analytics
- Display Longest Streak
- Exit

For example, to add a new habit, run the app and select "Add Habit" from the main menu then 
follow the CLI details of the habit you want. Once the habit is added, the user can complete the habit. Please
that in order for the time requirements to be triggered, the habit must be completed at least once.

# Run tests
- pip install -U pytest

# Author
@LinkedIn: '[Stilyan Petrov](https://www.linkedin.com/in/stilyan-petrov-a0b09a173/)'
