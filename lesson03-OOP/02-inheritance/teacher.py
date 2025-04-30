from person import Person

class Teacher(Person):
    def __init__(self, name, gender, age, seniority, subject):
        # calling the superclass constructor
        super().__init__(name, gender, age, seniority, subject)
    
    # methods of Teacher
    def teach(self):
        print(f"I am going to teach you {self.subject}")

    