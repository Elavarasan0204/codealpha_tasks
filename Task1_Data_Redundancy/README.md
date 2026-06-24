CodeAlpha Task 1 – Data Redundancy Removal System

Project Overview

This project is developed as part of the CodeAlpha Internship program under Cloud Computing.

The system identifies duplicate, redundant, and false positive data before storing records in a cloud database. It validates every new record against existing records and ensures that only unique and verified data is stored.

Technologies Used

- Python 3
- MySQL
- Railway Cloud Database
- VS Code

Features

- Detects duplicate ID entries
- Detects duplicate email entries
- Identifies false positive records
- Prevents redundant data storage
- Stores only unique records in cloud database

Working Process

1. User enters record details:
   
   - ID
   - Name
   - Email
   - Phone Number

2. System validates new data with existing database records.

3. Data classification:
   
   - Duplicate ID → Redundant
   - Duplicate Email → Redundant
   - Same Name with different details → False Positive
   - New Record → Unique

4. Only unique and verified records are inserted into the cloud database.

Database Structure

Table Name: records

Fields:

- id (Primary Key)
- name
- email (Unique)
- phone

Installation

1. Install Python 3
2. Install required package:

pip install mysql-connector-python

3. Configure Railway MySQL credentials in Python file
4. Run the program:

python task1_data_redundancy.py

Output

The program displays:

- UNIQUE
- REDUNDANT - Duplicate ID
- REDUNDANT - Duplicate Email
- FALSE POSITIVE

Conclusion

This project improves database accuracy and efficiency by preventing duplicate data entries and reducing redundancy in cloud storage.
