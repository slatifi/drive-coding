class Person:
    def __init__(self, name, gender, age, position):
        # attributes of person
        self.name = name
        self.gender = gender
        self.age = age
        self.position = position

    # methods of person
    def introduce(self):
        """Prints a message introducing themselves
        """
        print(f"My name is {self.name} and I am {self.age}")

    def change_position(self, new_position: str):
        """Assign the person a new position
        """
        self.position = new_position
        print(f"My new position is {self.position}")


