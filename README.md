# Create an Attendance Spreadsheet using Zoom reports.
I have fifty students. I need to know which ones are attending lectures. It's possible to download a usage report from Zoom for each class, but over a few class with many students this becomes a forboding aggregation. To complicate matters, students can log onto the class with a different name or user email.

# Python to the Rescue
I wrote a script to aggregate student names and emails and extend it by class dates. Rather than "yes/no" attendance, the table is instead filled with class attendance time (minutes). 

|       Name        |       Email        | 1-Sep | 3-Sep | 4-Sep | 8-Sep | 10-Sep | 11-Sep |
|-------------------|--------------------|-------|-------|-------|-------|--------|--------|
| Student 1         | student1@email.com |    45 |    55 |    55 |    15 |     50 |     35 |
| Student 2         |                    |       |       |    45 |       |        |     66 |
| Student 3         | stud3@email.com    |    15 |       |       |       |        |        |
| Student 3         | student3@email.com |    45 |       |    55 |    18 |     54 |        |
| Student Student 3 |                    |       |       |       |       |        |     45 |

This table aggregates 6 Zoom "Usage Report".

# Usage
Download Zoom Usage Reports for each class. Select both checkmark boxes. The reports may need to be renamed if the meeting is reoccurring. The meeting id is part of the filename. Save all reports to the same folder. They should be .csv files.

Change the directory in the script to the folder where the reports have been saved. 

Run script.

