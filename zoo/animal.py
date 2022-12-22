"""Animal class."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Class for creating an animal and holding information about it."""

    def __init__(self, name, age=1, gender="unknown"):
        """Inits class with:
        Required argument:
            name - string - name of the animal;
        Optional arguments:
            age=1 - or integer - age of the animal;
            gender="unknown" - male/female.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.fed_times = 0

    def eat(self):
        """Counts how many times the animal ate."""
        self.fed_times += 1

    @abstractmethod
    def is_hungry(self):
        """Returns boolean - whether the animal is currently hungry."""

    def __str__(self):
        return (f"{self.name} is a {self.age} years old {self.gender} "
                f"animal and was fed {self.fed_times} times")
