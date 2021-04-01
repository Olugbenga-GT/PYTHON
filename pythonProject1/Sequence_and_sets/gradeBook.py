grade_book = {
        'Susan': [92, 85, 100],
        'Eduardo': [83, 95, 79],
        'Azizi': [91, 89, 82],
        'Pantipa': [97, 91, 92]
            }
grade_total = 0;
grade_count = 0

for name, grade in grade_book.items():
    total = sum(grade)
    total_grade_count = len(grade)
    print(f' The total grade for {name} is {total} and the average is {total / total_grade_count:.2f}')
    grade_total = grade_total + total
    grade_count = total_grade_count + grade_count


print(f'The class total score is {grade_total} and the class average is {grade_total/grade_count:.2f}')

