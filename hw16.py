class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Employee):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


def test_team_lead_attributes():
    team_lead = TeamLead("Yurii", 80000, "QA Department", "Python", 5)

    print("Department:", team_lead.department)
    print("Programming Language:", team_lead.programming_language)
    print("Team Size:", team_lead.team_size)

    print("Тест пройдено успішно: всі атрибути доступні.")
test_team_lead_attributes()