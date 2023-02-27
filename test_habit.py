import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

from database import add_habit, complete_habit, increment_habit
from habit import Habit


class TestHabit(unittest.TestCase):

    def setUp(self):
        self.habit = Habit(name='test habit', category='test category', duration='test duration',
                           completed_habit='test date', database='test.db')

    def test_init(self):
        self.assertEqual(self.habit.name, 'test habit')
        self.assertEqual(self.habit.category, 'test category')
        self.assertEqual(self.habit.duration, 'test duration')
        self.assertEqual(self.habit.completed_habit, 'test date')
        self.assertEqual(self.habit.database, 'test.db')
        self.assertEqual(self.habit.streak, 0)
        self.assertEqual(self.habit.start_time, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.assertEqual(self.habit.end_time, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    @patch('builtins.print')
    @patch('habit.add_habit')
    def test_add_habit(self, mock_add_habit, mock_print):
        self.habit.add_habit('test.db')
        mock_add_habit.assert_called_once_with('test habit', 'test category', 'test duration', 0, self.habit.start_time)
        mock_print.assert_called_once_with("'test habit' habit was added successfully!")
        mock_print.assert_called_once_with("'test habit' habit was added successfully!")

        # Change the output of print to a custom message
        mock_print.assert_called_once_with("'test habit' habit was added successfully!")


    @patch('habit.complete_habit')
    @patch('habit.increment_habit')
    def test_complete_habit(self, mock_increment_habit, mock_complete_habit):
        self.habit.streak = 5
        self.habit.complete_habit('test.db')
        mock_complete_habit.assert_called_once_with('test habit', 5, self.habit.end_time)
        mock_increment_habit.assert_called_once_with('test habit')
