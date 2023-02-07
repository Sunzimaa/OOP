"""Zoo."""


class Animal:
    """Animal class."""
#0

    def __init__(self, name: str, specie: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param specie: animal specie
        """
        self.name = name
        self.specie = specie
        self.age = age


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.name = name
        self.max_animals = max_number_of_animals
        self.animals = []
        pass

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        if len(self.animals) == 0:
            return True
        elif animal in self.animals or len(self.animals) >= self.max_animals:
            return False
        else:
            for zoo_animal in self.animals:
                if animal.name == zoo_animal.name and animal.specie == zoo_animal.specie:
                    return False
                else:
                    return True
        pass

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal) is True:
            self.animals.append(animal)
        pass

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        if animal in self.animals:
            return True
        else:
            return False
        pass

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        if self.can_remove_animal(animal) is True:
            self.animals.remove(animal)
        pass

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals
        pass

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        animal_dict = {}
        for animal in self.animals:
            animal_dict[animal] = animal.age
        sorted_by_age = sorted(animal_dict, key=lambda x: x.age)
        return sorted_by_age
        pass

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        animal_dict = {}
        for animal in self.animals:
            animal_dict[animal] = animal.name
        sorted_by_name = sorted(animal_dict, key=lambda x: x.name)
        return sorted_by_name
        pass
