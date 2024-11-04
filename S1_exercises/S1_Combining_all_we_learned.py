# Exercise 15
list = [1,2,3,4,5,6,7,8,9,10]
list_squared = [i**2 for i in list]

# Exercise 16

Students = {"seleem":{
    "math": 2,
    "python": 3,
    "english": 4,
    "history": 3,},
"filipo":{
    "math": 4,
    "python": 3,
    "english": 4,
    "history": 1,},
"viktor":{
    "math": 1,
    "python": 2,
    "english": 2,
    "history": 4,}
}

def avg_grade(student):
    name = Students[student]
    grades = name.values()
    print(sum(grades) / len(grades))

# Exercise 16

def simple_calc(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "wrong operator"

a = float(input("a:"))
b = float(input("b:"))
operator = input("operator:")

print(simple_calc(a, b, operator))
