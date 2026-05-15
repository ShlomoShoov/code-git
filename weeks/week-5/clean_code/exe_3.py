def check_update(new_name,new_grade):

    status_dict = {'status':True, 'error':''}

    if not new_name or len(new_name) < 2:
        status_dict['status'] = False
        status_dict['error'] = 'Error: invalid name'
        
        
    
    elif new_grade < 0 or new_grade > 100:
        status_dict['status'] = False
        status_dict['error'] = 'Error: grade must be 0-100'
        
    
    return status_dict
    

def calculate_state(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    return total, average, top_count, failing_count

def print_report(names,grades,average,top_count,failing_count ):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

def save_to_file(names,grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")


def manage_students(names, grades, new_name, new_grade):
    # validation
    status_dict = check_update(new_name,new_grade)
    
    if not status_dict['status']:
        print(status_dict['erroe'])
        return

    # add student
    grades.append(new_grade)

     # calculate stats

    total, average, top_count, failing_count = calculate_state(grades)


    # print report
    print_report(names,grades,average,top_count,failing_count)


    # save to file

    save_to_file(names,grades)


    return names, grades
