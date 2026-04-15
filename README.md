# File-Based_Student_Management_System_Using_Python

This Python program is a Student Report Generator that stores and processes student academic data using a CSV file (students.csv). It provides a simple menu-driven interface for performing operations like adding student details, viewing records, and generating a ranked report.

The Add Student function allows the user to enter student details such as ID, name, and marks in subjects like Maths, Science, and English. These details are stored in the CSV file for permanent storage.

The View Students function reads the CSV file and displays all the stored student records in a simple format.

The Generate Report function is the core part of the program. It reads the data using DictReader, calculates the total and average marks for each student, and assigns grades based on performance. The grading system is:

A for average ≥ 90
B for average ≥ 75
C for average ≥ 50
D for average < 50

After processing, the program sorts all students based on their total marks in descending order and displays a ranked report, showing each student’s name, total marks, average, and grade.

The program runs continuously using a menu function until the user chooses to exit. It demonstrates important Python concepts such as file handling, dictionaries, sorting, loops, and conditional statements. This project is useful for beginners to understand how data can be stored, processed, and displayed efficiently.
