import sqlite3


def establish_connection(name='main.db'):
    """
    Creates a connection to the database
    """
    db = sqlite3.connect(name)
    create_table(db)
    return db


def create_table(db):
    """
    Creates a table in the database
    """
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits (
        habit_name TEXT NOT NULL,
        category TEXT NOT NULL, 
        duration TEXT NOT NULL,
        streak TEXT,
        start_time TEXT NOT NULL
        )''')
    db.commit()

    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits_data (
        habit TEXT NOT NULL,
        streak TEXT NOT NULL,
        end_time TEXT NOT NULL,
        FOREIGN KEY (habit) REFERENCES habits(habit_name))''')
    db.commit()


def add_habit(name, category, duration, streak, start_time):
    """Records a new habit into a table in the database

    Args:
        name (str): Name of the habit
        category (str): Preset category of the habit
        duration (str): Duration of the habit
        streak (int): Number of days the habit has been completed
        start_time (str): Date the habit was started
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute(
        '''INSERT INTO habits (habit_name, category, duration, streak, start_time) VALUES (?, ?, ?, ?, ?)''',
        (name, category, duration, streak, start_time))
    db.commit()


def remove_habit(name):
    """Removes the habit from the database with a given name by the CLI.
    Args:
        :param db:
        :param name:
    Returns:
        None
    Raises:
        None
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    # If the Habit is not found in the table, a message is printed to inform the user.
    cursor.execute('''DELETE FROM habits WHERE habit_name = ?''', (name,))
    if cursor.rowcount == 0:
        # If the Habit is not found in the table, a message is printed to inform the user.
        print(f"'{name}' was not found. You need first to add some habits.")
    else:
        # If the habit is found and removed successfully, a success message is printed.
        print(f"'{name}' habit was removed successfully!")
    db.commit()


def complete_habit(name, streak, end_time):
    """Updates the habit log

    Args:
        db (sqlite3.connect): _description_
        name (str): _description_
        finished (bool): _description_
        streak (int): _description_
        end_time (str): _description_
        :param streak:
        :param name:
        :param end_time:
        :param start_time:
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO habits_data (habit, streak, end_time) VALUES (?, ?, ?)''',
                   (name, streak, end_time))  # needs recording the end time, incrementing the streak to 1
    db.commit()


def increment_habit(name):
    """
    Increments the streak of the habit with the given name from the user.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute("UPDATE habits SET streak = streak + 1 WHERE habit_name = ?", (name,))
    cursor.execute("UPDATE habits_data SET streak = streak + 1 WHERE habit = ?", (name,))
    db.commit()


def habit_by_name(db, habit_name):
    """
    Returns a list of a habit by given name from the CLI.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE habit_name = ?''', (habit_name,))
    rows = cursor.fetchall()
    return rows


def display_all_habits(db):
    """
    Returns a list of all habits.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits''')
    habit_list = cursor.fetchall()
    return habit_list


def display_daily_habits(db):
    """
    Returns a list of all Daily habits to the CLI.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE duration='Daily' ''')
    daily_analysis = cursor.fetchall()
    return daily_analysis


def display_weekly_habits(db):
    """
    Returns a list of all Weekly habits to the CLI.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE duration='Weekly' ''')
    weekly_analysis = cursor.fetchall()
    return weekly_analysis


def display_monthly_habits(db):
    """
    Returns a list of all Monthly habits to the CLI.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE duration='Monthly' ''')
    monthly_analysis = cursor.fetchall()
    return monthly_analysis


def display_longest_streak(db):
    """
    Returns a single habit list with the longest streak.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT habit, MAX(streak) FROM habits_data''')
    longest_streak = cursor.fetchall()
    return longest_streak
