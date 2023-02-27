from database import *


def display_habit_name(db, habit_name):
    """
    Retrieve the habit with the specified name from the database and display its details.
    If habit is not found, prints an error message and returns a message in the CLI.
    """
    rows = habit_by_name(db, habit_name)
    if not rows:
        print(f"Your habit '{habit_name}' does not exist! "
              f"Please check your current habits and try again.")
        return None
    print(f"Your Habit '{habit_name}' recorded information is:")
    print("Habit Name".ljust(20), "Frequency".ljust(20), "Duration".ljust(20), "Streaks".ljust(20))
    for row in rows:
        print(row[0].ljust(20), row[1].ljust(20), row[2].ljust(20), row[3].ljust(20))
    return row


def get_habit_list(db):
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
        print(attribute[0].ljust(20), attribute[1].ljust(20), attribute[2].ljust(20), attribute[3].ljust(20))
    return attribute


def daily_habits(db):
    """
    Retrieve all daily habits from the database and display their details.
    If no daily habits are found, prints an error message and returns a message in the CLI.
    """
    analysis = display_daily_habits(db)
    if not analysis:
        print("No daily habits found. Please add a daily habit from the main menu.")
        return None
    print("Your Daily Habits:")
    print("Period".ljust(20), "Category".ljust(20), "Periodicity".ljust(20))
    for period in analysis:
        print(period[0].ljust(20), period[1].ljust(20), period[2].ljust(20))
    return period


def weekly_habits(db):
    """
    Retrieve all weekly habits from the database and display their details.
    If not weekly habits are found, prints an error message and returns and returns a message in the CLI.
    """
    analysis = display_weekly_habits(db)
    if not analysis:
        print("No weekly habits found! Please add a weekly habit from the main menu.")
        return None
    print("Your Weekly Habits are:")
    print("Habit".ljust(20), "Category".ljust(20), "Periodicity".ljust(20))
    for period in analysis:
        print(period[0].ljust(20), period[1].ljust(20), period[2].ljust(20))
    return period


def monthly_habits(db):
    """
    Retrieve all monthly habits from the database and display their details.
    If not monthly habits are found, prints an error message and returns message in the CLI.
    """
    analysis = display_monthly_habits(db)
    if not analysis:
        print("No monthly habits found! Please add a monthly habit from the main menu.")
        return None
    print("Your Monthly Habits are:")
    print("Habit".ljust(20), "Category".ljust(20), "Periodicity".ljust(20))
    for period in analysis:
        print(period[0].ljust(20), period[1].ljust(20), period[2].ljust(20))
    return period


def longest_streak(db):
    """
    Retrieve all monthly habits from the database and display their details.
    If not monthly habits are found, prints an error message and returns message in the CLI.
    """
    max_streak = display_longest_streak(db)
    if not max_streak:
        print("No streaks found.")
        return "Empty"
    for streak in max_streak:
        print(f"Your longest streak is {streak[1]} for habit '{streak[0]}'.")
        return streak
