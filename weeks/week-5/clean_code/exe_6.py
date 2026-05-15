def valid_name_and_grade(name, grade):
    status = {'is_valid': True, 'error': ''}
    if not name:
        status['is_valid'] = False
        status['error'] = 'Error: missing name'
    if not grade:
        status['is_valid'] = False
        status['error'] = f"Error: {name} has no grades"

    return status


def get_staticis(grades):
    total = sum(grades)
    average = total / len(grades)
    status = "pass" if average >= 56 else "fail"
    highest = max(grades)
    lowest = min(grades)
    return total, average, status, highest, lowest


def print_statistics(result_names, result_averages, result_statuses, result_lows, result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()


def print_passing_count(result_statuses, result_names):
    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")


def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]
        error_status = valid_name_and_grade(name, grades)
        if not error_status['is_valid']:
            print(error_status['error'])
            return

        total, average, status, highest, lowest = get_staticis(grades)

        result_names.append(name)
        result_averages.append(round(average, 1))
        result_statuses.append(status)
        result_highs.append(highest)
        result_lows.append(lowest)
    print_statistics(result_names, result_averages,
                     result_statuses, result_lows, result_highs)

    print_passing_count(result_statuses, result_names)
    return result_names, result_averages, result_statuses
