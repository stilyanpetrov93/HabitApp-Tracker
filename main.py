import analysis
import questionary as app
import database
from habit import Habit

# Welcoming message to the HabitApp Tracker
print("Welcome to your new habit app")
print("Good luck and wishing you many overcomed bad habits!")


def interface():
    """
    CLI interface using questionary python library
    to provide a self-contained CLI user menu
    for the Habit Tracker
    """
    # Defines the ten menu options for the user to select from and establishes the database connection
    db = database.establish_connection()

    choices = app.select(
        "What would you like to do?",
        choices=["Add a Habit",
                 "Remove a Habit",
                 "Complete a Habit",
                 "Search Habit by name",
                 "Display all habits",
                 "Display all Habits per Duration",
                 "Longest Habit streak by name",
                 "Display Longest Streak",
                 "Exit"
                 ]).ask()

    # Adding a Habit name, defining the category and duration
    if choices == "Add a Habit":
        name = app.text("What is the name of the habit you want to add?").ask()
        category = app.select("Choose your category your habit",
                              choices=["Productive Habit", "Social Habit", "Mental Habit",
                                       "Other Habit"]).ask()
        duration = app.select("How often do you want to complete this habit?",
                              choices=["Daily", "Weekly", "Monthly"]).ask()
        habit = Habit(name, category, duration)
        habit.add_habit(db)

    # Deleting a habit from the DB
    elif choices == "Remove a Habit":
        name = app.text("How did you call your Habit which you want to remove?").ask()
        database.remove_habit(name)

    # Completing a habit by typing the name of the habit
    elif choices == "Complete a Habit":
        name = app.text("How did you call your habit which you want to complete?").ask()
        habit = Habit(name)
        habit.complete_habit(db, name)

    # The user searches a habit by typing a name
    elif choices == "Search Habit by name":
        habit_name = app.text("How did you call your habit?").ask()
        analysis.display_habit_name(db, habit_name)

    # Option menu for displaying all currently tracked habits
    elif choices == "Display all habits":
        analysis.get_habit_list(db)

    # Displays a list of all habits by duration requested by the user
    elif choices == "Display all Habits per Duration":
        duration = app.select("What duration you want to display?",
                              choices=["Daily", "Weekly", "Monthly"]).ask()
        habit = Habit(duration)
        habit.display_habit_by_period()
        analysis.get_duration_habits(db, duration)

    # Displays the longest streak by requested name by the user
    elif choices == "Longest Habit streak by name":
        name = app.text("Type your Habit name to get the longest streak:").ask()
        habit = Habit(name, db)
        habit.longest_streak_by_name()
        analysis.get_max_streak(db, name)

    # Displays currently the longest streak habit
    elif choices == "Display Longest Streak":
        analysis.longest_streak(db)

    # Option for the user to terminate the CLI
    elif choices == "Exit":
        print("Goodbye")
        quit()


# A loop for the interface to run and accept user input until the user chooses to exit
if __name__ == "__main__":
    while True:
        interface()
