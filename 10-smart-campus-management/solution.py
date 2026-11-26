# Case Study 100: Comprehensive Smart Campus Management Simulation
# Syllabus used: conditional statements, loops, strings, lists, nested lists, tuples and tuple unpacking

# ---------------------------------------------------------------
# DATA
# ---------------------------------------------------------------
# student records stored as tuples: (roll no, name, attendance %, marks)
students = (
    ("26000709", "Rajulapati Venkanna Babu", 92, 78),
    ("26000710", "Anitha Rao", 68, 45),
    ("26000711", "Rakesh Kumar", 81, 62),
    ("26000712", "Sneha Sharma", 55, 34),
)

subjects = ["Maths", "Physics", "Programming"]

# nested list - subject wise marks of every student, in the same order as "students"
marks_matrix = [
    [78, 65, 82],
    [45, 52, 38],
    [62, 71, 58],
    [34, 41, 27],
]

# event registrations stored as tuples: (event code, student name)
registrations = (
    ("TECH1", "Anitha Rao"),
    ("CULT2", "Rakesh Kumar"),
    ("TECH1", "Sneha Sharma"),
    ("TECH1", "Anitha Rao"),
)

# nested list - resource name and its available quantity
resources = [
    ["Projector", 4],
    ["Laptop", 6],
    ["Speaker", 2],
    ["Whiteboard", 5],
]

MIN_ATTENDANCE = 75
PASS_MARK = 40

print("SMART CAMPUS MANAGEMENT SIMULATION")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("=" * 58)

running = True
while running:
    print()
    print("1. Student records")
    print("2. Attendance report")
    print("3. Marks and result")
    print("4. Event registration")
    print("5. Resource allocation")
    print("6. Summary report")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print()
        print("Roll No   Name                       Att%  Marks")
        print("-" * 58)
        for roll_no, name, attendance, marks in students:          # tuple unpacking
            print(roll_no.ljust(10), name.ljust(26), str(attendance).rjust(4), str(marks).rjust(6))
        print("-" * 58)
        print("Total students on record :", len(students))

    elif choice == "2":
        print()
        print("Attendance report (minimum required = " + str(MIN_ATTENDANCE) + "%)")
        print("-" * 58)
        eligible_count = 0
        for roll_no, name, attendance, marks in students:
            shortfall = MIN_ATTENDANCE - attendance
            if attendance >= MIN_ATTENDANCE:
                status = "ELIGIBLE"
                eligible_count = eligible_count + 1
            else:
                status = "NOT ELIGIBLE - short by " + str(shortfall) + "%"
            print(roll_no, name.ljust(26), str(attendance).rjust(4) + "% ", status)
        print("-" * 58)
        print("Attendance eligible     :", eligible_count, "out of", len(students))

    elif choice == "3":
        print()
        print("Subject wise marks (nested list)")
        print("-" * 58)
        header = "Name".ljust(26)
        for subject in subjects:
            header = header + subject.rjust(12)
        header = header + "  Result"
        print(header)
        failed_total = 0
        for i in range(len(students)):
            row = marks_matrix[i]
            line = students[i][1].ljust(26)
            failed = 0
            for j in range(len(row)):
                line = line + str(row[j]).rjust(12)
                if row[j] < PASS_MARK:
                    failed = failed + 1
            if failed == 0:
                result = "PASS"
            else:
                result = "FAIL in " + str(failed) + " subject(s)"
                failed_total = failed_total + 1
            print(line, " " + result)
        print("-" * 58)

        # subject wise average using the nested list
        for j in range(len(subjects)):
            total = 0
            for i in range(len(marks_matrix)):
                total = total + marks_matrix[i][j]
            print("  Average in", subjects[j].ljust(12), "=", round(total / len(marks_matrix), 2))
        print("Students with a backlog :", failed_total)

    elif choice == "4":
        print()
        print("Event registrations")
        print("-" * 58)
        seen = []
        for event_code, name in registrations:          # tuple unpacking
            if name in seen:
                print(event_code.ljust(8), name.ljust(26), "DUPLICATE ENTRY REJECTED")
            else:
                seen.append(name)
                print(event_code.ljust(8), name.ljust(26), "registered")

        # event wise count
        print("-" * 58)
        checked = []
        for event_code, name in registrations:
            if event_code not in checked:
                checked.append(event_code)
                count = 0
                for code, other_name in registrations:
                    if code == event_code:
                        count = count + 1
                print("  " + event_code, "->", count, "registration(s)")
        print("Total valid registrations :", len(seen))

    elif choice == "5":
        print()
        print("Resource allocation")
        print("-" * 58)
        request = input("Enter the resource name needed: ")
        quantity = int(input("Enter the quantity required: "))

        found = False
        index = 0
        while index < len(resources):
            resource_name, available = resources[index]        # nested list unpacking
            if resource_name == request:
                found = True
                if quantity <= 0:
                    print("REJECTED - quantity must be greater than zero")
                elif quantity > available:
                    print("PARTIAL - only", available, "unit(s) of", resource_name, "available")
                    print("Shortfall :", quantity - available, "unit(s)")
                    resources[index][1] = 0
                else:
                    resources[index][1] = available - quantity
                    print("ALLOCATED", quantity, "unit(s) of", resource_name)
                    print("Remaining :", resources[index][1], "unit(s)")
                break
            index = index + 1

        if found == False:
            print("INVALID - '" + request + "' is not a campus resource")
            print("Available resources :", end=" ")
            for item in resources:
                print(item[0], end=" ")
            print()

    elif choice == "6":
        print()
        print("CAMPUS SUMMARY REPORT")
        print("-" * 58)
        attendance_total = 0
        for roll_no, name, attendance, marks in students:
            attendance_total = attendance_total + attendance
        print("Average attendance      :", str(round(attendance_total / len(students), 2)) + "%")

        best_index = 0
        for i in range(1, len(students)):
            if students[i][3] > students[best_index][3]:
                best_index = i
        print("Best overall marks      :", students[best_index][1], "(" + str(students[best_index][3]) + ")")

        print("Events conducted        :", len(registrations), "registrations")
        print("Resources in store      :")
        for item in resources:
            print("   " + item[0].ljust(12), "->", item[1], "unit(s) left")

        low_attendance = ""
        for roll_no, name, attendance, marks in students:
            if attendance < MIN_ATTENDANCE:
                if low_attendance != "":
                    low_attendance = low_attendance + ", "
                low_attendance = low_attendance + name
        if low_attendance != "":
            print("Attendance warning      :", low_attendance)
        print("-" * 58)

    elif choice == "7":
        print("Exiting the smart campus simulation. Thank you.")
        running = False

    else:
        print("INVALID CHOICE - please enter a number from 1 to 7")
