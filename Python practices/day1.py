name = "kishore"
print(f"hello {name}")

age = 25 #int

salary = 50000.50 #float

is_working = True #bool

skills = ["Python", "AWS", "SQL"] #list

employee = {
    "id" : 6,
    "name": "kishore",
    "Designation" : "Data engineer"} #dict

print(skills)
print(employee)
print(salary)

def age(b): 
    return f"Age is {b}"

result = age(25)
print(result)

numbers = [1,2,3,4,5,6]
squares = [x*x for x in numbers]
print(squares)

a,b,c = input("Enter three words: ").split()
print(c)