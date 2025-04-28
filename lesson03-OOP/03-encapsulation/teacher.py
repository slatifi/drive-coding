from person import Person

class Teacher(Person):
    def __init__(self, name, gender, age, position, teach_subject):
        # attributes of Teacher
        super().__init__(name, gender, age, position)
        self.teach_subject = teach_subject
    
    # methods of Teacher
    def teach(self):
        """Prints a message of the subject the teacher is teaching
        """
        print(f"I am going to teach you {self.teach_subject}")


if __name__ == "__main__":

    john = Teacher("John", "Male", 34, "Maths", "Junior")

    john.introduce()
    john.teach()
    john.change_position("Senior")
    