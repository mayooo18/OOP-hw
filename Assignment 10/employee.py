class Employee:
    def __init__(self, employee_id, name, department, title):
        self._employee_id = employee_id
        self._name = name
        self._department = department
        self._title = title

    def get_employee_id(self): return self._employee_id
    def get_name(self): return self._name
    def get_department(self): return self._department
    def get_title(self): return self._title

    def set_name(self, name): self._name = name
    def set_department(self, department): self._department = department
    def set_title(self, title): self._title = title

    def __str__(self):
        return (f"Name: {self._name}\n"
                f"ID number: {self._employee_id}\n"
                f"Department: {self._department}\n"
                f"Title: {self._title}")
