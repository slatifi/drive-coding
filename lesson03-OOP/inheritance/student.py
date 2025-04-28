from person import Person

class Student(Person):
    def __init__(self, name, gender, age, position):
        # attributes of Student
        super().__init__(name, gender, age, position)

    # methods of Student
    def study(self):
        """Prints a message of saying that the student is studying
        """
        print(f"I am studying")


if __name__ == "__main__":

    sarah = Student("Sarah", "Female", 18, "1st year")

    sarah.introduce()
    sarah.study()
    sarah.change_position("2nd year")