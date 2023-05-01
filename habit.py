import database
import analysis
from datetime import datetime


class Habit:
    """
    Represents a habit that can be added to a database and tracked for completion.

    Attributes:
    ++++++++

    name: str
            The name of the habit.
    category: str
            The description of the habit.
    duration: str
            The duration of the habit.
    completed_habit: str
            The date the habit was completed.
    database: str
            The name of the database where the habit is stored.
    streak: int
            The current streak count for the habit.
    start_time: str
            The date and time the habit was started.
    end_time: str
            The date and time the habit was last completed.
            """

    def __init__(self, name: str = None, category: str = None, duration: str = None, database='main.db'):

        """
        Initializes a habit with the given name, category, duration, and database.

        Parameters:
        +++++++++++

        name: str
            The name of the habit.
        category: str
            The description of the habit.
        duration: str
            The duration of the habit.
        database: str
            The name of the database where the habit is stored.
        """

        self.complete_before = None
        self.db = None
        self.name = name
        self.category = category
        self.duration = duration
        self.database = database
        self.streak = 0
        self.start_time = datetime.now().strftime("%d/%m/%Y")
        self.end_time = datetime.now().strftime("%d/%m/%Y")

    def add_habit(self, db):
        """
         Records a new habit with specified name, category, duration, streak and start time specified in the cli.
        Parameters:
        +++++++++++
        db : str
        The name of the database where the habit will be added.
        """
        database.add_habit(self.name, self.category, self.duration, self.streak, self.start_time, self.end_time)
        if True:
            """
            Prints shows message that the habit was successfully added in the database.
            """
            print(f"'{self.name}' habit was added successfully!")


    def complete_habit(self, db, name):
        """
        Marks the specified habit as completed and increments the habit's streak by 1 in the database
        according to the time rules in the analysis.py file.

        Parameters:
        +++++++++++
        db : str
            The name of the database where the habit is stored.
        name : str
            The name of the habit to be completed.
        """
        if analysis.verify_duration(db, name) == 1:
            database.complete_habit(self.name, self.streak, self.end_time)
            database.increment_habit(self.name)
            print(f"You have completed the {name} habit!")
        elif analysis.verify_duration(db, name) == 2:
            print(f"You already completed {self.name} habit for the defined period! Please try again tomorrow!")
        elif analysis.verify_duration(db, name) == 0:
            database.reset_streak(db, name, self.end_time)
            print(f"Break the {name} habit! You have missed your completion. Your streak is set to 1! ")
        else:
            print(f"The '{name}' does not exists. Please verify your Habit name and remember "
                  f"the program is case  and word sensitive!")

    def reset_streak(self):
        """
        Resets the streak count to 1 when habit completion is missed for a specific period.
        """
        self.streak = 1

    def longest_streak_by_name(self):
        """
        Gets the longest streak for a specified habit name from the database.
        Parameters:
        +++++++++++

        db: str
            The name of the database where the habit is stored.
        name: str
            The name of the habit to get the longest streak for.
        """
        database.get_streak_by_name(self.db, self.name)

    def display_habit_by_period(self):
        """
        Displays all habits with specified duration from the CLI requested by the user.

        Parameters:
        +++++++++++

        db: str
            The name of the database where the habit is stored.
        duration: str
            The duration of the habits to display.
        """
        database.get_habit_periodicity(self.db, self.duration)
