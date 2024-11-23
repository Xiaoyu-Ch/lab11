import os
import matplotlib.pyplot as plt
from PIL import Image

def read_students(filename):
    students = {}
    with open(filename, 'r') as file:
        for line in file:
            id, name = line.strip().split(',')
            students[name] = id
    return students

def read_assignments(filename):
    assignments = {}
    with open(filename, 'r') as file:
        for line in file:
            id, name, points = line.strip().split(',')
            assignments[name] = {'id': id, 'points': int(points)}
    return assignments

def read_submissions(filename):
    submissions = []
    with open(filename, 'r') as file:
        for line in file:
            student_id, assignment_id, score = line.strip().split(',')
            submissions.append({
                'student_id': student_id,
                'assignment_id': assignment_id,
                'score': float(score)
            })
    return submissions

def calculate_student_grade(student_name, students, assignments, submissions):
    if student_name not in students:
        return "Student not found"
    
    student_id = students[student_name]
    total_points = 0
    earned_points = 0
    
    for submission in submissions:
        if submission['student_id'] == student_id:
            for assignment_name, assignment_data in assignments.items():
                if assignment_data['id'] == submission['assignment_id']:
                    total_points += assignment_data['points']
                    earned_points += assignment_data['points'] * (submission['score'] / 100)
    
    grade = (earned_points / total_points) * 100
    return f"{round(grade)}%"

def calculate_assignment_stats(assignment_name, assignments, submissions):
    if assignment_name not in assignments:
        return "Assignment not found"
    
    assignment_id = assignments[assignment_name]['id']
    scores = [sub['score'] for sub in submissions if sub['assignment_id'] == assignment_id]
    
    return f"Min: {min(scores)}%\nAvg: {round(sum(scores) / len(scores))}%\nMax: {max(scores)}%"

def display_assignment_graph(assignment_name, assignments, submissions):
    if assignment_name not in assignments:
        return "Assignment not found"
    
    assignment_id = assignments[assignment_name]['id']
    scores = [sub['score'] for sub in submissions if sub['assignment_id'] == assignment_id]
    
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(f"Score Distribution for {assignment_name}")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.savefig(f"{assignment_name}_histogram.png", dpi=300, bbox_inches='tight')
    plt.close()

def main():
    students = read_students('data/students.txt')
    assignments = read_assignments('data/assignments.txt')
    submissions = read_submissions('data/submissions.txt')

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    
    choice = input("Enter your selection: ")
    
    if choice == '1':
        student_name = input("What is the student's name: ")
        print(calculate_student_grade(student_name, students, assignments, submissions))
    elif choice == '2':
        assignment_name = input("What is the assignment name: ")
        print(calculate_assignment_stats(assignment_name, assignments, submissions))
    elif choice == '3':
        assignment_name = input("What is the assignment name: ")
        result = display_assignment_graph(assignment_name, assignments, submissions)
        if result:
            print(result)
        else:
            img = Image.open(f"{assignment_name}_histogram.png")
            img.show()

if __name__ == "__main__":
    main()
