class Teacher:
    def __init__(self, name, gender, age, teach_subject, position):
        # attributes of Teacher
        self.name = name
        self.gender = gender
        self.age = age
        self.teach_subject = teach_subject
        self.position = position
    
    # methods of Teacher
    def introduce(self):
        """Prints a message introducing themselves
        """
        print(f"My name is {self.name} and I am {self.age}")

    def change_position(self, new_position: str):
        """Assign the teacher a new position
        """
        self.position = new_position
        print(f"My new position is {self.position}")
    
    def teach(self):
        """Prints a message of the subject the teacher is teaching
        """
        print(f"I am going to teach you {self.teach_subject}")


if __name__ == "__main__":

    john = Teacher("John", "Male", 34, "Maths", "Junior")

    john.introduce()
    john.teach()
    john.change_position("Senior")

    