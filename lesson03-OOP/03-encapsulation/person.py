class Person:
    def __init__(self, name, gender, age, seniority, subject):
        # private attributes of person
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__seniority = seniority
        self.__subject = subject

    # methods of person
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age}")

    def promote(self, new_position: str):
        self.seniority = new_position
        print(f"My new position is {self.seniority}")

    # getter
    def get_name(self):
        return self.__name
    
    # setter
    def set_subject(self, new_subject):
        self.__subject = new_subject