import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import main


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        main.tasks.clear()

    def test_add_task(self):
        task = main.add_task("Купить молоко")
        self.assertEqual(task["title"], "Купить молоко")
        self.assertFalse(task["done"])
        self.assertEqual(len(main.list_tasks()), 1)

    def test_complete_task(self):
        main.add_task("Сделать лабу")
        self.assertTrue(main.complete_task(1))
        self.assertTrue(main.tasks[0]["done"])

    def test_complete_missing_task(self):
        self.assertFalse(main.complete_task(99))


if __name__ == "__main__":
    unittest.main()
