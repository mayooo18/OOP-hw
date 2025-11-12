# club_staff.py

class Staff:
    def __init__(self, name, department):
        self._name = name
        self._department = department

    def get_name(self):
        return self._name

    def get_department(self):
        return self._department

    def set_name(self, new_name):
        self._name = new_name

    def set_department(self, new_department):
        self._department = new_department

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay")

    def description(self):
        return f"{self._name} in {self._department}"


class Coach(Staff):
    def __init__(self, name, department, monthly_salary):
        super().__init__(name, department)
        self._monthly_salary = float(monthly_salary)

    def calculate_pay(self):
        return self._monthly_salary

    def get_monthly_salary(self):
        return self._monthly_salary

    def set_monthly_salary(self, new_salary):
        if new_salary > 0:
            self._monthly_salary = new_salary

    def description(self):
        return f"{self._name} coach monthly {self._monthly_salary:.2f}"


class Player(Staff):
    def __init__(self, name, department, base_pay, goals, goal_bonus):
        super().__init__(name, department)
        self._base_pay = float(base_pay)
        self._goals = int(goals)
        self._goal_bonus = float(goal_bonus)

    def calculate_pay(self):
        return self._base_pay + self._goals * self._goal_bonus

    
    def get_base_pay(self):
        return self._base_pay

    def get_goals(self):
        return self._goals

    def get_goal_bonus(self):
        return self._goal_bonus

    def set_base_pay(self, new_pay):
        if new_pay > 0:
            self._base_pay = new_pay

    def set_goals(self, new_goals):
        if new_goals >= 0:
            self._goals = new_goals

    def set_goal_bonus(self, new_bonus):
        if new_bonus >= 0:
            self._goal_bonus = new_bonus

    def description(self):
        return f"{self._name} player base {self._base_pay:.2f} goals {self._goals} bonus {self._goal_bonus:.2f} each"


class Medic(Staff):
    def __init__(self, name, department, hourly_rate, hours_worked):
        super().__init__(name, department)
        self._hourly_rate = float(hourly_rate)
        self._hours_worked = float(hours_worked)

    def calculate_pay(self):
        return self._hourly_rate * self._hours_worked

    
    def get_hourly_rate(self):
        return self._hourly_rate

    def get_hours_worked(self):
        return self._hours_worked

    
    def set_hourly_rate(self, new_rate):
        if new_rate > 0:
            self._hourly_rate = new_rate

    def set_hours_worked(self, new_hours):
        if new_hours >= 0:
            self._hours_worked = new_hours

    def description(self):
        return f"{self._name} physio rate {self._hourly_rate:.2f} hours {self._hours_worked:.1f}"
