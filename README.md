# Session 4: Basic Libraries I  

### Satellite Annotations Analysis  

In this session, you will analyze and organize satellite annotation files based on metadata encoded in their filenames. These files contain details such as date, satellite number, and unique regions, enabling you to extract meaningful insights.
---

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
