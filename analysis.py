#import habit
from database import *
from datetime import timedelta, datetime


def display_habit_name(db, name):
    """
    Retrieve the habit with the specified name from the database and display its details.
    If habit is not found, prints an error message and returns a message in the CLI.
    """
    rows = habit_by_name(name)
    if not rows:
        print(f"Your habit '{name}' does not exist! "
              f"Please check your current habits and try again.")
        return None
    print(f"Your Habit '{name}' recorded information is:")
    print("Habit Name".ljust(20), "Category".ljust(20), "Duration".ljust(20), "Streaks".ljust(20))
    for row in rows:
        print(str(row[1]).ljust(20), str(row[2]).ljust(20), str(row[3]).ljust(20), str(row[4]).ljust(20))
    return row


def get_habit_list(db):  # check what it displays, the rows are not accurate!!!
    """
    Retrieve habits list from the database and display their details.
    If no habits are found, prints an error message and returns a message in the CLI.
    """
    habit_list = display_all_habits(db)
    if not habit_list:
        print("Currently, you do not have any habits added! Please use the main menu to add a habit.")
        return None
    print("Your current Habits are:")
    print("Habit Name".ljust(20), "Category".ljust(20), "Duration".ljust(20), "Streaks".ljust(20))
    for attribute in habit_list:
        print(str(attribute[1]).ljust(20), str(attribute[2]).ljust(20), str(attribute[3]).ljust(20),
              str(attribute[4]).ljust(20))
    return attribute


def get_duration_habits(db, duration):
    """
    Retrieve all daily habits from the database and display their details.
    If no daily habits are found, prints an error message and returns a message in the CLI.
    """
    analysis = get_habit_periodicity(db, duration)
    if not analysis:
        print(f"No {duration} habits were found. Please add a {duration} habit from the main menu.")
        return None
    print(f"Your {duration} Habits are:")
    print("Habit name".ljust(20), "Category".ljust(20), "Duration".ljust(20), "Streaks".ljust(20))
    for period in analysis:
        print(period[1].ljust(20), period[2].ljust(20), period[3].ljust(20), period[4].ljust(20))
    return period


def get_max_streak(db, name):  # check what displays, the rows are not accurate!!!
    """
    Retrieve the habit with the specified name from the database and display the streaks.
    If habit is not found, prints an error message and returns a message in the CLI.
    """
    streak = get_streak_by_name(db, name)
    if not streak:
        print(f"Your habit '{name}' does not exist! "
              f"Please check your recorded habits and try again.")
        return None
    print(f"Your Habit '{name}' recorded information is:")
    for streaks in streak:
        print(f"Your Habit '{name}' has completed {str(streaks[0])} streaks.")
    return streaks


def longest_streak(db):
    """
    Retrieve all habits from the database and display only the habit with the longest streak.
    If no streaks are found, prints an error message and returns message in the CLI.
    """
    max_streak = display_longest_streak(db)
    # required the max calculation with Python due to an error in the database table (returns inaccurate max number)
    max_streaks = max([int(x[0]) for x in max_streak])
    habit_names = [x[1] for x in max_streak]
    if not max_streak:
        print("No streaks found.")
    print(f"Your longest streak is {max_streaks} for habit '{habit_names[1]}'.")
    return max_streak


def verify_duration(db, name):
    """
    Verifies the completion duration of the habit and returns a code to the habit.py file to either complete, return
    that the habit is already completed for the defined duration or the habit missed the time for completion.
    """
    verify = get_habits_data(db, name)
    for period in verify:
        duration = period[2]
        end_time = period[4]
        # checks the Daily completion requirements and returns the appropriate value to the habit.py file
        if duration == "Daily":
            if end_time is None:
                return 1  # returns a value to complete the habit
            elif datetime.now().date() == datetime.strptime(end_time, "%d/%m/%Y").date():
                return 2  # returns a value to display message: already completed habit for the period
            else:
                delta = datetime.now() - datetime.strptime(end_time, "%d/%m/%Y")
                delta_days = delta.days
                if delta_days >= 2:
                    return 0  # returns a value to display message that the user missed his completion
                elif delta_days < 2:
                    return 1
        # checks the Weekly completion requirements and returns the appropriate value to the habit.py file
        elif duration == "Weekly":
            if end_time is None:
                return 1
            elif datetime.now().date() == datetime.strptime(end_time, "%d/%m/%Y").date():
                return 2
            else:
                delta = datetime.now() - datetime.strptime(end_time, "%d/%m/%Y")
                delta_days = delta.days
                if delta_days >= 8:
                    return 0
                elif delta_days < 6:
                    return 2
                else:
                    return 1
        # checks the Monthly completion requirements and returns the appropriate value to the habit.py file
        elif duration == "Monthly":
            if end_time is None:
                return 1
            elif datetime.now().date() == datetime.strptime(end_time, "%d/%m/%Y").date():
                return 2
            else:
                delta = datetime.now() - datetime.strptime(end_time, "%d/%m/%Y")
                delta_days = delta.days
                if delta_days >= 31:
                    return 0
                elif delta_days < 29:
                    return 2
                else:
                    return 1
        return 3
