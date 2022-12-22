"""Classes for different animals."""

from animal import Animal
import random


class Lion(Animal):
    """Animal Lion - is always hungry."""

    def is_hungry(self):
        """Method returns whether the animal is currently hungry."""
        return True


class Monkey(Animal):
    """Animal Monkey is randomly hungry."""

    def is_hungry(self):
        """Method returns whether the animal is currently hungry."""
        return random.choice([True, False])


class Elephant(Animal):
    """Animal Elephant is hungry on every second occasion when a Worker checks on them"""

    def __init__(self, name, age=1, gender="unknown"):
        super().__init__(name, age, gender)
        self.check_count = 0

    def is_hungry(self):
        """Elephant is hungry on every second occasion when a Worker checks on them"""
        self.check_count += 1
        return self.check_count % 2 == 0
