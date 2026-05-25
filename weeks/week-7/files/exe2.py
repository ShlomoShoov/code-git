import os

# part 1

students = [
    ("Dan", [85, 90, 78]),
    ("MOMO", [92, 88, 95]),
    ("Yoni", [70, 65, 80]),
    ("Avi", [100, 95, 98]),
    ("Sara", [60, 72, 68]),
]

FILE_PATH = 'grades.txt'


def create_grades_file(filepath: str, students: list):
    """
    create or add to txt file a students grades, orederd in thet format:
        studenta name, grade, grade, ...

    parms:
        filepath: path to the file
        students: list of tuples with (student_name, [list of grades])

    """

    with open(filepath, 'a') as file:
        for student in students:
            name = student[0]
            grades = student[1]
            file.write(f'{name},')
            for grade in grades:
                file.write(f'{grade},')
            file.write('\n')


# create_grades_file(filepath=FILE_PATH, students=students)


def calc_grade_avarage(grades: list[str]) -> int:
    """
    reteun the avarge grade of a list of grades, take care to convert str to int and skip on non number values

    parms:
        grades: list of grades (str or int)
    return:
        average: the average grade, 0 if there is no grades in list


    """
    sum_of_grades = 0
    cnt_of_grades = 0

    for grade in grades:
        try:
            sum_of_grades += int(grade)
        except ValueError:
            continue
        else:
            cnt_of_grades += 1

    if cnt_of_grades == 0:
        average = 0
    else:
        average = sum_of_grades / cnt_of_grades

    return average


# part 2


def calculate_averages(filename: str) -> list[tuple]:
    """
    calaculate the avarage grade for any student in txt file in csv format
    parm:
        filename: (str) path to the student file

    return:
        list: list of tuples with (name, avetage grade)

    """
    avg_grades = []

    if not os.path.exists(path=filename):
        return avg_grades
    with open(filename, 'r') as file:

        for line in file:

            line = line.strip().split(',')

            if not line:
                continue

            name = line[0]

            if not name or len(line) <= 1:
                continue

            grades = line[1:]
            average = calc_grade_avarage(grades)

            avg_grades.append((name, average))

    return avg_grades


print(calculate_averages(filename=FILE_PATH))


# part 3

def save_results(averages: list, output_filename: str):
    """
    save the averages grades and names in a file, sorted from the highest to lowest
    """
    sorted_average = sorted(averages, key=lambda x: x[1], reverse=True)
    with open(output_filename, 'w') as file:
        for name, grade in sorted_average:
            file.write(f'{name},{grade}\n')


save_results(calculate_averages(filename=FILE_PATH), 'results.txt')


def get_statistics(averages: list):
    """
    calculat and return max_student, min_student, avg_grades, students_over_60

    parm:
        averages: list of name and average grade
    returns:
        max_student: (tuple) name and grade
        min_student: (tuple) name and grade
        avg_grades: (int)
        students_over_60: (tuple) student over 60 and all students


    
    """



    max_student = max(averages, key=lambda x: x[1])
    min_student = min(averages, key=lambda x: x[1])
    cnt_of_student = len(averages)
    sun_of_grades = sum([grade[1] for grade in averages])
    avg_grades = sun_of_grades / cnt_of_student
    students_over_60 = (len(
        [student for student in averages if student[1] >= 60]),cnt_of_student)
    return max_student, min_student, avg_grades, students_over_60

def append_statistics(averages: list, filename: str):

    """
    calculate statistics about avarage grades and append the results to the file provied
    Class average: 
    Highest: 
    Lowest: 
    Passing (>=60):


    """
    if not averages:
        return
    max_student, min_student, avg_grades, students_over_60 = get_statistics(averages)
    
    
    with open(filename, 'a') as file:
        file.write('=== Student Results ===\n')
        file.write(f'max grade : {max_student[1]} - {max_student[0]}\n')
        file.write(f'min grade : {min_student[1]} - {min_student[0]}\n')
        file.write(f'average grade : {avg_grades}\n')
        file.write(f'student pass {students_over_60[0]}/{students_over_60[1]}\n')

append_statistics(calculate_averages(filename=FILE_PATH), 'results.txt')
