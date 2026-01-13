class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def status(self):
        return f"Ο/Η {self.name} έχει βαθμό {self.grade}"

# Δημιουργία αντικειμένου.
s1 = Student("Γιώργος", 18)
print(s1.status())