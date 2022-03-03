recuStudents = []
with open('arquivo.txt') as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(' ')
        if int(student_grade[1]) < 6:
            recuStudents.append(student_grade[0] + '\n')

with open('arquivoRecu.txt', mode='w') as recuStudentsFile:
    print(recuStudents)
    recuStudentsFile.writelines(recuStudents)