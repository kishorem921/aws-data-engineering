employees = [
    "rahul",
    "priya",
    "karthik",
    "arun",
    "meena"
]

for employee in employees:
    print(employee.upper())

employees_1 =[{"id": 1, "name": "rahul", "designation": "developer"},
              {"id": 2, "name": "priya", "designation": "tester"},
              {"id": 3, "name": "karthik", "designation": "manager"}
]

for employee in employees_1:
    employee["name"] = employee["name"].upper()

print(employees_1)