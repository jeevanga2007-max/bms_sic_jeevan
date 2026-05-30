import pandas as pd
df = pd.read_csv("data_students.csv")

name = input("Enter student name: ")

student = df[df.iloc[:, 0] == name]

if student.empty:
    print("Student not found")
    exit()

student = student.iloc[0]
question_columns = df.columns[1:]
total_questions = len(question_columns)
correct_answers = student[question_columns].sum()
percentage = (correct_answers / total_questions) * 100

if percentage >= 80:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "D"

module1_score = student.iloc[1:6].sum()
module2_score = student.iloc[6:11].sum()
module3_score = student.iloc[11:16].sum()
module4_score = student.iloc[16:21].sum()

module1_percentage = (module1_score / 5) * 100
module2_percentage = (module2_score / 5) * 100
module3_percentage = (module3_score / 5) * 100
module4_percentage = (module4_score / 5) * 100

highest = max(
    module1_percentage,
    module2_percentage,
    module3_percentage,
    module4_percentage
)

lowest = min(
    module1_percentage,
    module2_percentage,
    module3_percentage,
    module4_percentage
)

if highest == module1_percentage:
    best_module = "Module 1"

elif highest == module2_percentage:
    best_module = "Module 2"

elif highest == module3_percentage:
    best_module = "Module 3"

else:
    best_module = "Module 4"

if lowest == module1_percentage:
    weak_module = "Module 1"

elif lowest == module2_percentage:
    weak_module = "Module 2"

elif lowest == module3_percentage:
    weak_module = "Module 3"

else:
    weak_module = "Module 4"

# DIFFICULTY ANALYSIS
# Each module:
# Q1,Q2 -> Easy
# Q3,Q4 -> Moderate
# Q5 -> Difficult

easy_score = (
    student.iloc[1] +
    student.iloc[2] +
    student.iloc[6] +
    student.iloc[7] +
    student.iloc[11] +
    student.iloc[12] +
    student.iloc[16] +
    student.iloc[17]
)

moderate_score = (
    student.iloc[3] +
    student.iloc[4] +
    student.iloc[8] +
    student.iloc[9] +
    student.iloc[13] +
    student.iloc[14] +
    student.iloc[18] +
    student.iloc[19]
)

difficult_score = (
    student.iloc[5] +
    student.iloc[10] +
    student.iloc[15] +
    student.iloc[20]
)

easy_percentage = (easy_score / 8) * 100
moderate_percentage = (moderate_score / 8) * 100
difficult_percentage = (difficult_score / 4) * 100


print("\n========== RESULT ANALYSIS ==========")

print(f"\nStudent Name: {name}")

print(f"Total Questions: {total_questions}")

print(f"Correct Answers: {correct_answers}")

print(f"Percentage: {percentage:.2f}%")

print(f"Grade: {grade}")


print("\n----- Module Analysis -----")

print(f"Module 1 Score: {module1_percentage:.2f}%")

print(f"Module 2 Score: {module2_percentage:.2f}%")

print(f"Module 3 Score: {module3_percentage:.2f}%")

print(f"Module 4 Score: {module4_percentage:.2f}%")

print(f"\nBest Module: {best_module}")

print(f"Weakest Module: {weak_module}")


print("\n----- Difficulty Analysis -----")

print(f"Easy Questions Score: {easy_percentage:.2f}%")

print(f"Moderate Questions Score: {moderate_percentage:.2f}%")

print(f"Difficult Questions Score: {difficult_percentage:.2f}%")

print("\n====================================")