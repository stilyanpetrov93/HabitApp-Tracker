import sqlite3


def establish_connection(name='main.db'):
    """
    Creates a connection to the database.
    Args:
        name (str): The name of the database to connect to. Defaults to 'main.db'.

    Returns:
        sqlite3.Connection: A connection to the specified database.
    """
    db = sqlite3.connect(name)
    create_table(db)
    return db


def create_table(db):
    """
    Creates a table in the database.
    Args:
        db (sqlite3.Connection): A connection to the database.
    """
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        duration TEXT,
        start_time TEXT,
        end_time TEXT,
        FOREIGN KEY (habit) REFERENCES habits(habit_name))''')
    db.commit()

    cursor = db.cursor()
    cursor.execute('''CREATE TRIGGER IF NOT EXISTS habits_data_insert_trigger
AFTER INSERT ON habits_data
BEGIN
    UPDATE habits_data SET 
        start_time = (SELECT start_time FROM habits WHERE habit_name = NEW.habit),
        duration = (SELECT duration FROM habits WHERE habit_name = NEW.habit)
    WHERE rowid = NEW.rowid;
END
''')
    db.commit()


def add_habit(name, category, duration, streak, start_time, end_time):
    """Records a new habit into a table in the database.

    Args:
        name (str): The name of the habit to add.
        category (str): The category of the habit to add.
        duration (str): The duration of the habit to add.
        streak (int): The current streak of the habit to add.
        start_time (str): The start time of the habit to add.
        #complete_before (str): The completion time of the habit to add.
        end_time (str): The end time of the habit to add.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute(
        '''INSERT INTO habits (habit_name, category, duration, streak, start_time) 
        VALUES (?, ?, ?, ?, ?)''',
        (name, category, duration, streak, start_time))
    cursor.execute(
        '''INSERT INTO habits_data (habit, streak, start_time)
        VALUES (?, ?, ?)''',
        (name, streak, start_time))
    db.commit()


def remove_habit(name):
    """
    Removes the habit from the database with a given name by the CLI.
    Args:
        name (str): Name of the habit to remove
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM habits WHERE habit_name = ?''', (name,))
    if cursor.rowcount == 0:
        # If the Habit is not found in the table, a message is printed to inform the user.
        print(f"'{name}' was not found. You need first to add some habits.")
    else:
        # If the habit is found and removed successfully, a success message is printed.
        print(f"'{name}' habit was removed successfully!")
    db.commit()


def complete_habit(name, streak, end_time):
    """Updates the end_time in the database table which relies on the time completion verification.

    Args:
        name (str): Name of the habit to update.
        streak (int): Number of days the habit has been completed.
        end_time (str): Date the habit was last completed.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE habits_data SET end_time = ? WHERE habit = ?''', (end_time, name))
    db.commit()


def increment_habit(name):
    """
    Increments the streak of the habit with the given name by the user.
    Args:
        name (str): The name of the habit to increment.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute("UPDATE habits SET streak = streak + 1 WHERE habit_name = ?", (name,))
    cursor.execute("UPDATE habits_data SET streak = streak + 1 WHERE habit = ?", (name,))
    db.commit()


def habit_by_name(name):
    """
    Returns a list of a habit by given name from the CLI.
    Args:
        name (str): The name of the habit to retrieve.

    Returns:
        A list of tuples representing the habit matching the given name.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE habit_name = ?''', (name,))
    rows = cursor.fetchall()
    return rows


def display_all_habits(db):
    """
    Returns a list of all active habits.
    Args:
        db (sqlite3.connect): A connection to the SQLite database.

    Returns:
        A list of tuples representing all active habits in the database. Each tuple
        contains the habit name, its category, its duration and its current streak.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits''')
    habit_list = cursor.fetchall()
    return habit_list


def get_habits_data(db, name):
    """
    Returns all recorded data from the database by given name from the user in CLI.
    Args:
        db (sqlite3.connect): A connection to the database.
        name (str): The name of the habit to retrieve data for.

    Returns:
        A list of dictionaries containing data for the given habit. Each dictionary contains the following keys:
            'duration': The duration of the habit in minutes.
            'end_time': The timestamp of the end time of the habit.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits_data WHERE habit = ? ''', (name,))
    all_habits = cursor.fetchall()
    rows = []
    for row in rows:
        habit_dict = {
            'duration': row[2],
            'end_time': row[4],
        }
        all_habits.append(habit_dict)
    return all_habits


def get_streak_by_name(db, name):
    """
    Returns the max for a habit name requested by the user through the CLI.
    Args:
        db (sqlite3.connect): A connection to the database.
        name (str): The name of the habit to retrieve the streak for.

    Returns:
        An integer representing the longest streak of the given habit.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT MAX(streak), habit FROM habits_data WHERE habit = ? GROUP BY streak''', (name,))
    streak = cursor.fetchall()
    return streak


def display_longest_streak(db):
    """
    Returns a single habit line with the longest streak.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT MAX(streak), habit FROM habits_data GROUP BY streak''')
    longest_streak = cursor.fetchall()
    return longest_streak


def get_habit_periodicity(db, duration):
    """
    Returns a list of all habit by given periodicity requested from the CLI.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM habits WHERE duration = ? ''', (duration,))
    habits_duration = cursor.fetchall()
    return habits_duration


def reset_streak(db, name, end_time):
    """
    Resets the streak of a habit when the user misses the completion of a habit and sets the value to 1.

    Parameters:
    db (str): The name of the database.
    name (str): The name of the habit.
    end_time (str): The end time of the habit.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE habits SET streak = 1 WHERE habit_name = ?''', (name,))
    cursor.execute('''UPDATE habits_data SET streak = 1 WHERE habit = ?''', (name,))
    cursor.execute('''UPDATE habits_data SET end_time = ? WHERE habit = ?''', (end_time, name))
    db.commit()
