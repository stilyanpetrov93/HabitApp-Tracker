from datetime import datetime
from database import *


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

    def __init__(self, name: str = None, category: str = None, duration: str = None, complete_habit: str = None,
                 database='main.db'):

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
        completed_habit: str
            The date the habit was completed.
        database: str
            The name of the database where the habit is stored.
        """

        self.db = None
        self.name = name
        self.category = category
        self.duration = duration
        self.completed_habit = complete_habit
        self.database = database
        self.streak = 0
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")



    def add_habit(self, db):
        """
        Records a new habit with specified name, category, duration, streak and start time specified in the cli
        """
        add_habit(self.name, self.category, self.duration, self.streak, self.start_time)
        if True:
            """
            Prints shows message that the habit was successfully added in the database.
            """
            print(f"'{self.name}' habit was added successfully!")


    def complete_habit(self, db):
        """
        Marks the habit as completed and increments the habit streak by 1 in the database.
        """
        complete_habit(self.name, self.streak, self.end_time)
        increment_habit(self.name)
        if True:
            """
            Prints shows message that the habit was successfully incremented/completed in the database table.
            """
            print(f"'{self.name}' has been completed.")