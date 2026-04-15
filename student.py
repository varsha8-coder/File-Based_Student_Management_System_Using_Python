import csv
def add_student():
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        maths = int(input("Maths: "))
        science = int(input("Science: "))
        english = int(input("English: "))
        
        writer.writerow([sid, name, maths, science, english])

def view_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def generate_report():
    students = []
    
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total = int(row['Maths']) + int(row['Science']) + int(row['English'])
            avg = total / 3
            
            if avg >= 90:
                grade = 'A'
            elif avg >= 75:
                grade = 'B'
            elif avg >= 50:
                grade = 'C'
            else:
                grade = 'D'
            
            students.append({
                "name": row['Name'],
                "total": total,
                "avg": avg,
                "grade": grade
            })

    students.sort(key=lambda x: x['total'], reverse=True)
    
    print("--- Report ---")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} - Total: {s['total']}, Avg: {s['avg']:.2f}, Grade: {s['grade']}")

def menu():
    while True:
        print("1. Add Student2. View Students\n3. Generate Report\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

menu()
