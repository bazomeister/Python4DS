# Session 5: Processing and Organizing Annotation Files  

## Overview  
This session focuses on processing annotation files stored in a directory. The tasks include counting annotations, grouping them by month, saving the data in different formats, and organizing it for more efficient analysis. Through these exercises, you will practice file handling, datetime manipulation, and data serialization using formats like JSON and Pickle.  

---

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
