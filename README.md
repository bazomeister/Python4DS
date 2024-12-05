# Python for Data Science - Weekly Exercises

This repository will contain the weekly exercises from the **Python for Data Science** course. Each week, new exercises will be added and building upon the concepts covered in the sessions.

---

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

---

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

---

## Session 3

### Object Oriented Programming
This session focused on Object-Oriented Programming (OOP) in Python. It introduced key concepts such as classes, objects, attributes, and methods. The primary objective was to understand how to structure programs using classes and create objects that model real-world entities. The session covered OOP principles like abstraction, inheritance, and encapsulation code.

---

# Session 4: Basic Libraries I  

### Satellite Annotations Analysis  

In this session, you will analyze and organize satellite annotation files based on metadata encoded in their filenames. These files contain details such as date, satellite number, and unique regions, enabling you to extract meaningful insights.

### Exercises  

Given a zip file with a subfolder containing multiple annotations, where the naming convention for each file is:  
```
{DATE}_{TIME}SN{SATELLITE_NUMBER}QUICKVIEW_VISUAL{VERSION}{UNIQUE_REGION}.txt
```
in which:
- **DATE**: Expressed as `YYYYMMDD` (year, month, and day), e.g., `20241201`, `20230321`...  
- **TIME**: Expressed as `HHMMSS` (hour, minutes, and seconds), e.g., `2134307`.  
- **SATELLITE_NUMBER**: An integer representing the satellite number.  
- **VERSION**: Indicates the pipeline version, e.g., `"0_1_2"`, `"1_3_1"`.  
- **UNIQUE_REGION**: Specifies a unique location in the form of a string, e.g., `SATL-2KM-10N_552_4164`.  

**Exercises:**  
1. Determine the total number of files in the annotations folder.  
2. Count how many files follow the naming convention expressed above.  
3. Calculate the number of annotations per month and year, and identify the month with the most annotation files.  
4. Create a new annotations folder with subfolders corresponding to each month.  
5. Print all the annotations, sorted from the most recent to the oldest.  
6. Analyze satellites:  
   - Count the total number of different satellites.  
   - Determine how many annotations exist for each satellite.  
   - Identify which satellite was used in the most recent annotation file.  
7. Count the total number of unique regions.  

---

# Session 5: Processing and Organizing Annotation Files  

## Overview  
This session focuses on processing annotation files stored in a directory. The tasks include counting annotations, grouping them by month, saving the data in different formats, and organizing it for more efficient analysis. Through these exercises, you will practice file handling, datetime manipulation, and data serialization using formats like JSON and Pickle.  

## Exercises  

1. **Count Annotations Per Month and Year**  
   - **Task**: Count the number of annotation files for each month and year using dates extracted from filenames. Find the month with the most annotations and present the data in a sorted table.  

2. **Save Data in Multiple Formats**  
   a. **Save Data in JSON Format**  
      - Group annotations by month into a dictionary where:  
        - Each key represents a month.  
        - Each value is a list of annotation filenames corresponding to that month.  
        - Save the dictionary as a JSON file and reload it to verify the data.  
   b. **Save Data in Pickle Format**  
      - Save the same grouped dictionary in Pickle format, a binary format. Reload the file and display the data in a tabular format to confirm its accuracy.  
   c. **Enhance Data with Names and Dates**  
      - Modify the grouped dictionary so that each entry for a month contains:  
        - A list of dictionaries, where each dictionary includes; name and date   
      - Save the enhanced structure as a JSON file for detailed and future-proof data representation.  

3. **Sort Annotations from the Second Half of 2024**  
   - Extract and sort annotations from the second half of 2024. Display the filenames and corresponding dates in chronological order.
     
---

# Session 6: Pandas I  

## Overview  
This session focuses on analyzing two datasets: Netflix and Titanic. Below is a summary of the exercises and their objectives using Pandas methods.  

## Netflix Dataset Exercises  

1. **Identify Missing Ratings**  
   - **Task**: Count the number of missing values in each column to assess the completeness of the data.  

2. **Films from 2021 in Your Country**  
   - **Task**: Replace missing values in the 'country' column with "Unknown" and identify films from 2021 that correspond to your country.  

3. **Movies from 2020 with Complete Information**  
   - **Task**: Filter the dataset to find movies from 2020 that have all necessary data fields populated.  

4. **Year with the Most Titles**  
   - **Task**: Determine which year had the highest number of entries in the dataset.  

5. **Average Annual Releases Since 2010**  
   - **Task**: Calculate the average number of titles released each year since 2010.  

## Titanic Dataset Exercises  

1. **Gender-Based Survival Percentage**  
   - **Task**: Calculate the survival rate for each gender by dividing the number of survivors by the total number of passengers in each gender group.  

2. **Survival Percentage by Gender and Class**  
   - **Task**: Compute survival rates for each combination of gender and passenger class to analyze trends across groups.  

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

# Session 8: Data Visualization with Seaborn  

## Overview  
In this session, we use Python's Seaborn library to visualize and analyze a dataset containing information about students, such as their study time, grades, courses, gender, and more. Each exercise focuses on creating a specific type of plot to derive insights from the data.  

## Exercises  

1. **Lineplot: Study Time by Student Name**  
   Create a lineplot to visualize how study time varies by student and identify the student with the highest study time.  

2. **Histogram: Grade Distribution**  
   Create a histogram (histplot) to visualize the frequency distribution of grades and determine which grade range has the highest frequency of students.  

3. **ECDF Plot: Cumulative Grade Distribution**  
   Plot an ECDF (ecdfplot) to show the cumulative percentage of grades and calculate the percentage of students scoring below 85.  

4. **Stripplot: Grade Distribution by Course**  
   Create a stripplot to visualize individual grade distributions for each course and identify the course with the most spread in grades.  

5. **Swarmplot: Gender and Study Time**  
   Plot a swarmplot to analyze the relationship between gender and study time and determine which gender has a higher average study time.  

6. **Pointplot: Average Grade by Course**  
   Create a pointplot to compare the average grade across courses and identify the course with the highest average grade.  
