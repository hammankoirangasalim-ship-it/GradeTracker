print("=== STUDENT GRADE CALCULATOR ===")

# 1. Capture User Inputs
student_name = input("Enter student name: ")
assignment_score = input("Enter assignment score (out of 100): ")
exam_score = input("Enter exam score (out ot 100): ")

# 2. Convert Text Strings to Math Decimals (floats)
score1 = float(assignment_score)
score2 = float(exam_score)

# 3. Calculate the Average
final_grade = (score1 + score2) / 2

# 4. Display the Final Report Card
print("\n--- FINAL REPORT CARD ---")
print("Student Name:", student_name)
print("Final Averag Score:", final_grade)

print("Grade tracking session completed successfully!")


      