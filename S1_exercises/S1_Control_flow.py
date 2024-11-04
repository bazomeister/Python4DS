# Exercise 8
number = int(input())

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# Exercise 9
number = [1,2,3,4,5]
for i in number:
    print(i)

# Exercise 10
counter = 1
while counter <= 5:
 print(counter)
 counter += 1

# Exercise 11

grade = input(str())

if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good Job!")
elif grade == "C":
    print("fair.")
elif grade == "D":
    print("Needs Improvement.")
elif grade == "F":
    print("Failing.")
else:
    print("Invalid Grade")