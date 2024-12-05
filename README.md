# Python for Data Science - Weekly Exercises

This repository will contain the weekly exercises from the **Python for Data Science** course. Each week, new exercises will be added and building upon the concepts covered in the sessions.

## Session 1: Exercises

Session 1 focuses on Python basics like printing, variables, loops, lists, and simple functions. These tasks help me become comfortable with Python's core concepts.

### 1. **Print a Greeting**
   - Print a simple greeting message using Python.

### 2. **Basic Arithmetic**
   - Perform basic arithmetic operations with variables.

### 3. **String Manipulation**
   - Work with string formatting and variable assignment.

### 4. **Lists**
   - Create and manipulate lists by accessing and printing elements.

### 5. **Dictionaries**
   - Create a dictionary and print key-value pairs.

### 6. **Tuples**
   - Define a tuple and access its elements.

### 7. **Sets**
   - Create and manipulate sets by adding, removing, and merging elements.

### 8. **Conditional Statements**
   - Use `if`, `elif`, and `else` to make decisions based on user input.

### 9. **For Loop**
   - Iterate through a list using a `for` loop.

### 10. **While Loop**
   - Implement a `while` loop to print numbers in a sequence.

### 11. **Match Statement (Python 3.10+)**
   - Use a `match` statement to map user input to specific output.

### 12. **Define a Function**
   - Write a simple function to greet a user by name.

### 13. **Function with Return Value**
   - Define a function that returns the square of a number.

### 14. **Function with Default Parameters**
   - Write a function that multiplies two numbers, with a default value for one parameter.

### 15. **List Comprehension**
   - Use list comprehension to create a new list from an existing one.

### 16. **Nested Data Structures**
   - Work with nested dictionaries and lists to calculate averages.

### 17. **Simple Calculator**
   - Build a basic calculator that performs arithmetic operations based on user input.


## Session 2: Exercises
In this session, the focus is on working with Python environments, version control using Git, and setting up an IDE. The exercises include tasks like creating a FizzBuzz function, filtering data, building a simple to-do list, and a temperature converter.

### 1. **FizzBuzz**
   - Write a function `fizzbuzz(n)` that prints:
     - "Fizz" for multiples of 3
     - "Buzz" for multiples of 5
     - "FizzBuzz" for multiples of both 3 and 5
     - The number itself for other numbers (1 to 20)

### 2. **Basic Data Filtering**
   - Create a list of mixed data types (integers, strings, and floats).
   - Use list comprehension to filter out only the integers.

### 3. **Simple To-Do List**
   - Create an empty list called `todo_list`.
   - Define functions to add tasks and display tasks.

### 4. **Temperature Converter**
   - Write a function `celsius_to_fahrenheit(celsius)` that converts Celsius to Fahrenheit.
   - Output the conversion for specific temperatures.


## Session 3

### Object Oriented Programming
This session focused on Object-Oriented Programming (OOP) in Python. It introduced key concepts such as classes, objects, attributes, and methods. The primary objective was to understand how to structure programs using classes and create objects that model real-world entities. The session covered OOP principles like abstraction, inheritance, and encapsulation code.


## Session 4

## Overview
Session 4 provides am introduction to foundational Python libraries for data science. It covers numpy for numerical operations, scipy for scientific computing, and key utility libraries such as math, os, glob, and shutil.

Exercises:
- File Count: Count the total number of files in the annotations folder.
- Naming Convention Compliance: Identify how many files adhere to the specified naming format.
- Annotations by Month and Year: Count the annotations per month and year, and determine which month has the highest number.
- Organize by Month: Create a new directory structure, organizing annotation files into folders by month.
- Sort and Print Annotations: List all annotations from the most recent to the oldest.
- Satellite Analysis: Identify the number of unique satellites, count annotations per satellite, and find the satellite used in the most recent annotation.
- Unique Regions: Count how many distinct regions are represented across the annotations.

---

## Session 5

Session 5 explores essential Python libraries, including handling the data formats JSON, Pickle, and Parquet, using the _re_ library, and working with time and DateTime. 

Exercises:
- Annotations by Month and Year: Count the number of annotations per month and year, and determine the month with the most annotations (similar to the previous session).
- Dictionary Creation and Storage:
   - Create a dictionary in which each key represents a month, and each value is a list of annotation filenames for that month.
   - Save this dictionary in JSON format, reload it, and verify its contents.
   - Save the dictionary in Pickle format.
   Modify the dictionary structure to store a dictionary with name and date (using a DateTime object) for each annotation.
- Sorted Annotations for Specific Timeframe: Print all annotations from the second half of 2024, ordered from the oldest to the newest

---

# Session 7: DataFrame Manipulations with Pandas  

## Overview  
This session focuses on performing various DataFrame manipulations using Python's pandas library. The tasks involve creating new columns, merging DataFrames, and extracting specific details from text columns. These exercises aim to enhance your data preprocessing and transformation skills.  

## Exercises  

1. **Creating Professor Initials**  
   - Extract the initials of each professor's first and last names and store them in a new column called `professor_initials`.  

2. **Join DataFrames on Professor Column**  
   - Combine the original DataFrame with a new DataFrame (`df_courses`) using the `professor` column as the key.  

3. **Merge DataFrames to Include Course Information**  
   - Merge the original DataFrame and `df_courses` based on the common `professor` column to add course information for each professor.  

4. **Extract Professor Last Names**  
   - Use string operations to extract the last name of each professor from the `professor` column and store it in a new column called `professor_last_name`.  

   ---

