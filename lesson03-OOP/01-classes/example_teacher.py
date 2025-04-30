class Teacher:
    def __init__(self, name, gender, age, subject, seniority):
        # attributes of Teacher
        self.name = name
        self.gender = gender
        self.age = age
        self.seniority = seniority
        self.subject = subject
    
    # methods of Teacher
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age}")
    
    def teach(self):
        print(f"I am going to teach you {self.subject}")
    
    def promote(self, new_position: str):
        self.seniority = new_position
        print(f"My new position is {self.seniority}")


if __name__ == "__main__":

    john = Teacher("John", "Male", 34, "Maths", "Junior")

    john.introduce()
    john.teach()
    john.promote("Senior")
