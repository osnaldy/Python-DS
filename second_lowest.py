students = []

n = int(input("Enter the number of students "))

for i in range(n):

    name = input("Name: ")
    score = int(input("Score: "))
    students.append([name, score])
students.sort()

grade = set([line[1] for line in students])
grade.remove(min(grade))
mini = min(grade)

for i in range(len(students)):

    if students[i][1] == mini:

        print(students[i][0])

