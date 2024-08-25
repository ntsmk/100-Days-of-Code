student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for i in student_scores:
    if student_scores[i] >= 91:
        student_scores[i] = "Outstanding"
    elif student_scores[i] >= 81:
        student_scores[i] = "Exceeds Expectations"
    elif student_scores[i] >= 71:
        student_scores[i] = "Acceptable"
    elif student_scores[i] < 70:
        student_scores[i] = "Fail"

student_grades = student_scores

print(student_grades)
