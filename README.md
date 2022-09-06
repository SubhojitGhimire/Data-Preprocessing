# Data-Preprocessing

Data Preprocessing for Excel CSV Files  
Generating Output of thousands of csv data in row-wise format  
```
Given Two Columns- First Column: File_Name or Article_Name. Second Column: Text_Data  
```
```
Output: First Row First Column: File_Name. Second Column: Text_Data_1
Output: Second Row First Column: File_Name. Second Column: Text_Data_2 and so on for all thousands of rows
```

### EXAMPLE  
Existing Document to pre-process  ```**test_data_0.csv**```  
```
DOC     TEXT
doc1    Hello World | This is a Test Data | To show the working of this program
doc2    This is continuation | This is second row data
doc3    Unlike the first two rows    This Data is separated by multiple spaces    This is an example
```
After running the code  ```**output_test_data.csv**```  
```
DOC     TEXT
doc1    Hello World
doc1    This is a Test Data
doc1    To show the working of this program
doc2    This is continuation
doc2    This is second row data
doc3    Unlike the first two rows
doc3    This Data is separated by multiple spaces
doc3    This is an example
```
