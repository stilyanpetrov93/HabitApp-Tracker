from os import name

import pytest

from habit import Habit
from database import *

from freezegun import freeze_time


@pytest.fixture(scope='module')
def database():
    print("\n-----SETUP-----\n")
    database = establish_connection("test.db")
    print("Created temporary test.db for test purpose.\n")
    print("Initiating tests.....\n")
    yield database
    print("-----TEARDOWN-----")
    print("\nClosing connection with test database...\n")
    database.close()
    print("Connection successfully terminated!")
    import os
    os.remove("test.db")
    print("\nDeleted test.db file.")
    print("\nTest completed successfully")


def test_add(database):
    habit = Habit("Coding", "Other Habit", "Daily")
    habit.add_habit(name)
    habit = Habit("Overreacting", "Mental Habit", "Daily")
    habit.add_habit(name)
    habit = Habit("Running", "Productive Habit", "Weekly")
    habit.add_habit(name)
    habit = Habit("Smoking", "Other Habit", "Daily")
    habit.add_habit(name)
    habit = Habit("Socialize", "Mental Habit", "Monthly")
    habit.add_habit(name)
    habit = Habit("Negativity", "Mental Habit", "Weekly")
    habit.add_habit(name)
    habit = Habit("No alcohol", "Other Habit", "Weekly")
    habit.add_habit(name)


# Completing all added habit to trigger the time rule
def test_complete():
    db = sqlite3.connect('test.db')
    habit = Habit("Coding")
    habit.complete_habit(db, "Coding")
    habit = Habit("Overreacting")
    habit.complete_habit(db, "Overreacting")
    habit = Habit("Running")
    habit.complete_habit(db, "Running")
    habit = Habit("Smoking")
    habit.complete_habit(db, "Smoking")
    habit = Habit("Socialize")
    habit.complete_habit(db, "Socialize")
    habit = Habit("Negativity")
    habit.complete_habit(db, "Negativity")
    habit = Habit("No alcohol")
    habit.complete_habit(db, "No alcohol")
    # intentinal incorrect habit name entered for completion
    habit = Habit("Drinking alcohol")
    habit.complete_habit(db, "Drinking alcohol")


# in the time frame completion + one day
@freeze_time("17/04/2023")
def test_complete_scenario_1():
    db = sqlite3.connect('test.db')
    habit = Habit("Overreacting")
    habit.complete_habit(db, "Overreacting")


# plus 7 days from now - completes the habit
@freeze_time("22/04/2023")
def test_complete_scenario_2():
    db = sqlite3.connect('test.db')
    habit = Habit("Running")
    habit.complete_habit(db, "Running")


# Intentional incorrect habit name
def test_complete_scenario_3():
    db = sqlite3.connect('test.db')
    habit = Habit("Smokink")
    habit.complete_habit(db, "Smokink")  # incorrect habit name


# plus 30 days from now - completes the habit
@freeze_time("15/05/2023")
def test_complete_scenario_4():
    db = sqlite3.connect('test.db')
    habit = Habit("Socialize")
    habit.complete_habit(db, "Socialize")


# plus 9 days from now - missed habit completion
@freeze_time("25/04/2023")
def test_complete_scenario_5():
    db = sqlite3.connect('test.db')
    habit = Habit("Negativity")
    habit.complete_habit(db, "Negativity")


# plus 2 days from now - already completed habit
@freeze_time("18/04/2023")
def test_complete_scenario_6():
    db = sqlite3.connect('test.db')
    habit = Habit("No alcohol")
    habit.complete_habit(db, "No alcohol")


# removing all habits from the test.db before deleting the file
def test_remove():
    db = sqlite3.connect('test.db')
    remove_habit("Coding")
    remove_habit("Overreacting")
    remove_habit("Running")
    remove_habit("Smoking")
    remove_habit("Socialize")
    remove_habit("Negativity")
    remove_habit("No alcohol")

    remove_habit("Drinking alcohol")
    db.close()
