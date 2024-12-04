# Session 5  
## Basic Libraries II  

In this session, I worked with annotation files stored in a directory and performed various data processing tasks. I counted and grouped annotations by month, saved the data in different formats, and organized it for easier analysis. Through this process, I applied file handling techniques, manipulated datetime objects, and utilized data serialization methods using JSON and Pickle.

### Exercises  

Reusing the same annotations from the previous session, complete the following tasks using the libraries covered in this session:  

1. **Annotations by Month and Year**  
   - Count the number of annotations per month and year.  
   - Identify which month has the highest number of annotation files.  

2. **Organize Annotations by Month**  
   a. Create a dictionary where each **key** is a month, and the corresponding **value** is a list of annotation names with dates that correspond to that month.  
   b. Save the dictionary in JSON format, then load it again to ensure the data was saved and loaded correctly.  
   c. Save the dictionary using Pickle as a binary format.  
   d. Enhance the data by modifying the dictionary so that, instead of a list of annotation names, each annotation is represented as a dictionary with the following keys:  
      - **name**: The annotation filename.  
      - **date**: The date (as a datetime object) extracted from the filename.  

3. **Sort Annotations from the Second Half of 2024**  
   - Print all the annotations from the second half of 2024 (June to December), sorted from the oldest to the newest.  
