class Person:
    """Person Class
    
    Attributes:
        first_name: str
        last_name:str
        email: default None
        DOB: str
    
    Methods:
        greet() -> str
        get_age() -> int
    """

    def __init__(self, first_name: str, last_name: str, DOB: str):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.email = None
    
    def greet(self):
        return f"Hello, my name is {self.first_name} {self.last_name}"
    
    def get_age(self):
        pass


class Teacher(Person):
    """Teacher Class
    
    Attributes:
        OCT_pin: int
        school: str
        email_k12: str
        classes: List[Class]
    
    Methods:
        assign_work(Class) -> void
        greet() -> void
        add_class(class) -> void
        remove_class(class) -> void
    """

    def __init__(self, OCT_pin: int, school: str, email_k12: str, classes: List[Class]):
        self.OCT_pin = OCT_pin
        self.school = school
        self.email_k12 = email_k12
        self.classes = classes
    
    def assign_work(self, classes):
        pass

    def greet(self):
        pass


class Student(Person):
    """Student Class
    
    Attributes:
        email_k12: str
        student_num: int
    
    Methods:
        greet() -> void
    """

    def __init__(self, email_k12: str, student_num: int):
        self.email_k12 = email_k12
        self.student_num = student_num
    
    def greet(self):
        pass


class Class:
    """Class class
    
    Attributes:
        subject: str
        student_list: List[Student]
    
    Methods:
        add_student(student) -> void
        reomve_student(student) -> void
    """

    def __init__(self, subject: str, student_list: List[Student]):
        self.subject = subject
        self.student_list = student_list
    
    def add_student(self, student: Student):
        pass

    def reomve_student(self, student: Student):
        pass
