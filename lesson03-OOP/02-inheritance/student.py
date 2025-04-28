from person import Person

class Student(Person):
    def __init__(self, name, gender, age, position, subject):
        # attributes of Student
        super().__init__(name, gender, age, position)
        self.subject_to_study = subject

    # methods of Student
    def study(self):
        """Prints a message of saying that the student is studying
        """
        print(f"I am studying {self.subject_to_study}")


if __name__ == "__main__":

    sarah = Student("Sarah", "Female", 18, "1st year", "Maths")

    sarah.introduce()
    sarah.study()
    sarah.change_position("2nd year")