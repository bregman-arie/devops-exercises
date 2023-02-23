## Class 0x00 - Solution

1. write a simple class that has two attributes of which one has a default value and has two methods

```python
from typing import Optional
""" Student Module

    """


class Student:
    def __init__(self, name: str, department: Optional[str] = None) -> None:
        """ Instance Initialization function

        Args:
            name (str): Name of student
            department (Optional[str], optional): Department. Defaults to None.
        """
        self.name = name
        self.department = department

    def getdetails(self) -> str:
        """ Gets the students details

        Returns:
            str: A formatted string
        """
        return f"Name is {self.name}, I'm in department {self.department}"

    def change_department(self, new_deparment: str) -> None:
        """Changes the department of the student object

        Args:
            new_deparment (str): Assigns the new deparment value to dept attr
        """
        self.department = new_deparment

# student1 instantiation
student1 = Student("Ayobami", "Statistics")

print(student1.getdetails())

# Calling the change_department function to change the department of student
student1.change_department("CS")

print(student1.department)
```

Output

```
Name is Ayobami, I'm in department Statistics
CS
```
