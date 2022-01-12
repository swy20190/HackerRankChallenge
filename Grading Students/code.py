import os


def gradingStudents(grades):
    # Write your code here
    answer = []
    for grade in grades:
        if grade < 38:
            answer.append(grade)
        else:
            next_five = (int(grade / 5) + 1) * 5
            if next_five - grade < 3:
                answer.append(next_five)
            else:
                answer.append(grade)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
