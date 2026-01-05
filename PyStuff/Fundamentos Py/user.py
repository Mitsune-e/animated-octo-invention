class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"