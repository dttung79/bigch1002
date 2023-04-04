students = {}

while True:
    print('1. Add student')
    print('2. Print all students')
    print('3. Find best/worst student')
    print('4. Update student')
    print('5. Remove student')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        name = input('Enter name: ')
        if name in students:
            print('Student already exists')
        else:
            GPA = float(input('Enter score: '))
            students[name] = GPA
    elif choice == 2:
        for name, GPA in students.items():
            print(f'{name:10}: {GPA:5.2f}')
    elif choice == 3:
        best_student = max(students, key=students.get)
        worst_student = min(students, key=students.get)
        print(f'Best student: {best_student}, GPA: {students[best_student]}')
        print(f'Worst student: {worst_student}, GPA: {students[worst_student]}')
    elif choice == 4:
        name = input('Enter name: ')
        if name in students:
            print('Current GPA:', students[name])
            GPA = float(input('Enter new GPA: '))
            students[name] = GPA
        else:
            print('Student does not exist')
    elif choice == 5:
        name = input('Enter name: ')
        if name in students:
            del students[name]
        else:
            print('Student does not exist')
    else:
        break