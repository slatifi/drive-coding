class Person:
    def __init__(self, name, gender, age, seniority, subject):
        # attributes of person
        self.name = name
        self.gender = gender
        self.age = age
        self.seniority = seniority
        self.subject = subject

    # methods of person
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age}")

    def promote(self, new_position: str):
        self.seniority = new_position
        print(f"My new position is {self.seniority}")


