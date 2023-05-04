class Student:
    name="Leila"
    age=20
    nationality="Rwandese"
    country="Rwanda"
    first_name="Leila"
    last_name="Ashur"
    
class Student:
    school="Akirachix"
    def __init__(self,name,age,nationality,country,first_name,last_name,year_of_birth):
        self.name=name
        self.age=age
        self.nationality=nationality
        self.country=country
        self.first_name=first_name
        self.last_name=last_name
        self.year_of_birth=year_of_birth
      
    def greet_student(self):
        return f"Hello {self.name},welcome to {self.school} am pround to be an {self.nationality}"
    
    def full_name(self):
      return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
          current_year=2023
          return current_year-self.age
    def show_initials(self):
      return f"{self.first_name[0]}.{self.last_name[0]}."
