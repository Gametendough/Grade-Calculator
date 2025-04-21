# V2
import matplotlib.pyplot as plt
import os


def load_students(file_name):
    students = {}
    with open(file_name, 'r') as f:
        for line in f:
            student_id = line[:3] 
            student_name = line[3:].strip() 
            students[student_id] = student_name
    return students

def load_assignments(file_name):
    assignments = {}
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):  
            name = lines[i].strip()  
            assignment_id = lines[i + 1].strip() 
            points = int(lines[i + 2].strip()) 
            assignments[name] = (assignment_id, points) 
    return assignments


def calculate_grade(student_id, submissions, assignments):
    total_earned_points = 0
    for file_name in os.listdir(submissions):
        file_path = os.path.join(submissions, file_name)
        with open(file_path, 'r') as f:
            for line in f:
                sub_student_id, assignment_id, percentage = line.split('|')
                if sub_student_id == student_id:
                    points = next((value[1] for key, value in assignments.items() if value[0] == assignment_id), 0)
                    total_earned_points += (int(percentage) / 100) * points
    grade_percentage = round((total_earned_points / 1000) * 100)
    return grade_percentage

def option_2(assignment_name, assignments, submissions_folder):
    assignment_data = assignments.get(assignment_name, None)
    if not assignment_data:
        print("Assignment not found.")
        return

    assignment_id, _ = assignment_data  
    scores = []
    for file_name in os.listdir(submissions_folder):
        file_path = os.path.join(submissions_folder, file_name)
        with open(file_path, 'r') as f:
            for line in f:
                _, sub_assignment_id, percentage = line.split('|')
                if sub_assignment_id == assignment_id:
                    scores.append(int(percentage))

    if scores:
        min_score = min(scores)
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        print(f"Min: {int(min_score)}%")
        print(f"Avg: {int(avg_score)}%")
        print(f"Max: {int(max_score)}%")
    else:
        print(f"No submissions found for {assignment_name}.")


def option_3(assignment_name, assignments, submissions_folder):
    assignment_data = assignments.get(assignment_name, None)
    if not assignment_data:
        print("Assignment not found.")
        return

    assignment_id, _ = assignment_data 
    scores = []
    for file_name in os.listdir(submissions_folder):
        file_path = os.path.join(submissions_folder, file_name)
        with open(file_path, 'r') as f:
            for line in f:
                _, sub_assignment_id, percentage = line.split('|')
                if sub_assignment_id == assignment_id:
                    scores.append(int(percentage))

    if not scores: 
        print(f"No submissions found for {assignment_name}.")
        return

    plt.hist(scores, bins=[50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
    plt.show()

if __name__ == "__main__":
    students = load_students('students.txt')
    assignments = load_assignments('assignments.txt')

    print("1. Student grade\n2. Assignment statistics\n3. Assignment graph")
    user_input = input("\nEnter your selection: ")

    if user_input == "1":
        student_name = input("What is the student's name: ")
        student_id = next((id for id, name in students.items() if name.lower() == student_name.lower()), None)
        if student_id:
            grade = calculate_grade(student_id, 'submissions', assignments)  
            print(f"{grade}%")
        else:
            print("Student not found.")
    elif user_input == "2":
        assignment_name = input("What is the assignment name: ")
        option_2(assignment_name, assignments, 'submissions') 
    elif user_input == "3":
        assignment_name = input("Enter the assignment name: ")
        option_3(assignment_name, assignments, 'submissions')  
    else:
        print("Invalid selection. Please try again.")

