"""Worker class."""

from animals import *


class Worker:
    """The worker class, that looks after animals."""

    def __init__(self, name, animals_to_look_after=[]):
        """Inits class with:
        Required argument - name - string;
        Optional argument - animals_to_look_after=[] - list of animals instances.
    """
        self.name = name
        self.animals_to_look_after = animals_to_look_after

    def do_daily_routine(self):
        """Checks if animal from the list is hungry and feed it if True."""
        for animal in self.animals_to_look_after:
            if animal.is_hungry():
                animal.eat()

    def add_animal(self, animal):
        """To add animal to the list."""
        self.animals_to_look_after.append(animal)
