import datetime
from typing import List


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
        self._first_name = first_name
        self._last_name = last_name
        self.DOB = DOB
        self._email = None
    
    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, value: str):
        self._first_name = value
    
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, value: str):
        self._last_name = value
    
    def greet(self):
        return f"Hello, my name is {self._first_name} {self._last_name}."
    
    def get_age(self):
        pass


class Teacher(Person):
    """Teacher Class
    
    Attributes:
        OCT_pin: int
        school: str
        email_k12: str
        classes: List[Classroom]
    
    Methods:
        assign_work(Class) -> void
        greet() -> void
        add_class(class) -> void
        remove_class(class) -> void
    """

    def __init__(self, first_name: str, last_name: str, DOB: str, OCT_pin: int,
    school: str, email_k12: str, classes: List[Classroom]):
        super().__init__(first_name)
        super().__init__(last_name)
        self._DOB = DOB
        self._OCT_pin = OCT_pin
        self._school = school
        self._email_k12 = email_k12
        self._classes = classes
    
    def get_DOB(self):
        return self._DOB

    def set_DOB(self, value: str):
        self._DOB = value
    
    def get_OCT_pin(self):
        return self._OCT_pin
    
    def set_OCT_pin(self, value: int):
        self._OCT_pin = value

    def get_school(self):
        return self._school
    
    def set_school(self, value: str):
        self._school = value
    
    def get_email_k12(self):
        return self._email_k12
    
    def set_email_k12(self, value: str):
        self._email_k12
    
    def get_classes(self):
        return self._classes
    
    def set_classes(self, value: List[Classroom]):
        self._classes = value

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

    def __init__(self, first_name: str, last_name: str, DOB: str, email_k12: str, student_num: int):
        super().__init__(first_name)
        super().__init__(last_name)
        self._DOB = DOB
        self._email_k12 = email_k12
        self._student_num = student_num
    
    def get_DOB(self):
        return self._DOB
    
    def set_DOB(self, value: str):
        self._DOB = value
    
    def get_email_k12(self):
        return self._email_k12
    
    def set_email_k12(self, value: str):
        self._email_k12 = value
    
    def get_student_num(self):
        return self._student_num
    
    def set_student_num(self, value: int):
        self._student_num = value
    
    def greet(self):
        pass


class Classroom:
    """Classroom Class
    
    Attributes:
        subject: str
        student_list: List[Student]
    
    Methods:
        add_student(student) -> void
        reomve_student(student) -> void
    """

    def __init__(self, subject: str, student_list: List[Student]):
        self._subject = subject
        self._student_list = student_list
    
    def get_subject(self):
        return self._subject
    
    def set_subject(self, value: str):
        self._subject = value
    
    def get_student_list(self):
        return self._student_list
    
    def set_student_list(self, value: List[Student]):
        self._student_list = value

    def add_student(self, student: Student):
        pass

    def reomve_student(self, student: Student):
        pass
