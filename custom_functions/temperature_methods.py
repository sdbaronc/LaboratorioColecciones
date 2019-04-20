


def calculate_final_temperature(student_grades_list):
    grade_sum = 0
    grade_count = len(student_grades_list)


    for grade in student_grades_list:
        grade_sum += grade


    final_grade = grade_sum / grade_count

    return final_grade


def calculate_best_temperature(student_grades_list):

    best_grade = student_grades_list[0]


    for grade in student_grades_list:

        if grade > best_grade:
            best_grade = grade


    return best_grade


def remove_worst_temperature(student_grades_list):

    worst_grade = student_grades_list[0]
    worst_grade_position = 0


    grades_count = len(student_grades_list)


    grade_sum = 0





    position_count = 0

    for grade in student_grades_list:


        if grade < worst_grade:

            worst_grade_position = position_count
            worst_grade = grade


        position_count += 1


    student_grades_list.pop(worst_grade_position)


    return student_grades_list
