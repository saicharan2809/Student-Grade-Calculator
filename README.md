# Student-Grade-Calculator

🔎 Summary of Your Code
I have created a simple Student Grade Calculator using Python.
The program:
	1.	Takes five subject marks as input from the user (`a`, `b`, `c`, `d`, `e`).
	2.	Adds up all the marks to calculate the total (`f`).
	3.	Determines the grade based on the total marks:
	•	`Grade A` if the total is 95 or more.
	•	`Grade B` if the total is 75 or more (but less than 95).
	•	`Grade C` if the total is 50 or more (but less than 75).
	•	`Grade D` if the total is less than 50.
	4.	Prints the total marks earned.
	5.	Calculates and prints the average marks (`f/5`).

📌 Variables Used
Let’s go through each variable:
	•	`a, b, c, d, e` → These are the marks input by the user, one for each subject. Each `input()` is converted into an integer using `int()`.
	•	`f` → This stores the total marks, calculated by adding all five subject marks:


The program uses if-elif-else logic to assign grades:
	1.	`if f >= 95:` Prints “Grade A”.
	2.	`elif f >= 75:` Prints “Grade B”.
	3.	`elif f >= 50:` Prints “Grade C”.
	4.	`if f < 50:` (This acts like an `else` in your current code) Prints “Grade D”.

📌 Output
Your program prints two key details:
	•	Total Marks: `f`
	•	Average Marks: `f/5`

🎯 Final Thought
You have successfully implemented a basic grading system in Python using:
	•	Variables (`a, b, c, d, e, f`)
	•	Arithmetic Operators (`+`, `/`)
	•	Conditional Statements (`if`, `elif`, `else`)
	•	Input/Output (`input()`, `print()`)
This is a strong foundation for moving toward more advanced programs like handling multiple students, validating marks, or automating grades with real grading criteria.
