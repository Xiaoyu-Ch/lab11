from course_data import actual_data

def calculate_student_grade(data, student_name):
    roster = data['roster']
    assignments = data['assignments']

    if student_name not in roster:
        return [], 'Student not found.'

    total_score = 0
    total_weight = 0
    results = []

    for assignment_name, assignment_data in assignments.items():
        weight = assignment_data['weight']
        submissions = assignment_data['submissions']
        score = submissions.get(student_name, 0)  # Default to 0 if no submission

        results.append(f"{assignment_name}: {score}%")
        total_score += score * (weight / 100)
        total_weight += weight

    if total_weight > 0:
        total_grade = total_score / total_weight * 100
    else:
        total_grade = 0

    return results, round(total_grade, 1)

def main():
    student_name = input("Enter the student's name: ")
    results, total_grade = calculate_student_grade(actual_data, student_name)

    if isinstance(total_grade, str):
        print(total_grade)
    else:
        for result in results:
            print(result)
        print(f'Total grade: {total_grade:.1f}%')

if __name__ == "__main__":
    main()