from person import Person

class Student(Person):
    def __init__(self, name, gender, age, seniority, subject, chapter):
        # calling the superclass constructor
        super().__init__(name, gender, age, seniority, subject)
        # specific attributes of Student
        self.chapter = chapter

    # methods of Student
    def study(self):
        print(f"I am studying chapter {self.chapter} of {self.subject}")