class Student:
    def __init__(self, name, gender, age, position):
        # attributes of Student
        self.name = name
        self.gender = gender
        self.age = age
        self.position = position

    # methods of Student
    def introduce(self):
        """Prints a message introducing themselves
        """
        print(f"My name is {self.name} and I am {self.age}")

    def change_position(self, new_position: str):
        """Assign the student a new position
        """
        self.position = new_position
        print(f"My new position is {self.position}")
    
    def study(self):
        """Prints a message of saying that the student is studying
        """
        print(f"I am studying")


if __name__ == "__main__":

    sarah = Student("Sarah", "Female", 18, "1st year")

    sarah.introduce()
    sarah.study()
    sarah.change_position("2nd year")