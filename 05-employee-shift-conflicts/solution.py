# Case Study 48: Tuple-Based Employee Shift Conflict Detection
# Syllabus used: variables, operators, conditional statements, loops, strings, lists, tuples,
#               tuple operations and unpacking

print("EMPLOYEE SHIFT CONFLICT DETECTION")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 58)

# each shift is a tuple: (employee, day, start_hour, end_hour)
shifts = [
    ("E101", "Monday", 9, 13),
    ("E102", "Monday", 10, 15),
    ("E101", "Monday", 14, 18),
    ("E103", "Tuesday", 9, 12),
    ("E102", "Tuesday", 12, 17),
    ("E104", "Wednesday", 8, 12),
    ("E104", "Wednesday", 11, 16),
    ("E105", "Thursday", 13, 18),
]

print("Shift register")
for employee, day, start, end in shifts:          # tuple unpacking
    print("  " + employee, "|", day.ljust(10), "|", str(start).rjust(2) + ":00 to", str(end).rjust(2) + ":00")
print("-" * 58)

MIN_GAP = 2          # minimum rest hours allowed between two shifts of the same employee
conflicts = []

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):
        emp1, day1, start1, end1 = shifts[i]
        emp2, day2, start2, end2 = shifts[j]

        if emp1 == emp2 and day1 == day2:
            if start1 <= start2:
                earlier_end = end1
                later_start = start2
            else:
                earlier_end = end2
                later_start = start1

            if later_start < earlier_end:
                kind = "OVERLAP"
            elif later_start - earlier_end < MIN_GAP:
                kind = "INSUFFICIENT REST (" + str(later_start - earlier_end) + " h)"
            else:
                kind = "OK"

            if kind != "OK":
                conflicts.append((emp1, day1, start1, end1, start2, end2, kind))
                print("Conflict :", emp1, "on", day1, "->", kind)

print("-" * 58)

if len(conflicts) == 0:
    print("Result : no scheduling conflicts found")
else:
    print("Total conflicts found :", len(conflicts))
    for employee, day, start1, end1, start2, end2, kind in conflicts:      # tuple unpacking
        print("  " + employee, day, "shifts", str(start1) + "-" + str(end1),
              "and", str(start2) + "-" + str(end2), "->", kind)

# employees whose schedule is clean
clean = []
for employee, day, start, end in shifts:
    found = False
    for conflict in conflicts:
        if conflict[0] == employee:
            found = True
    if found == False:
        if employee not in clean:
            clean.append(employee)

print("-" * 58)
print("Employees without any conflict :", clean)

# which employee has the most conflicts
worst_employee = ""
worst_count = 0
checked = []
for conflict in conflicts:
    employee = conflict[0]
    if employee not in checked:
        checked.append(employee)
        count = 0
        for other in conflicts:
            if other[0] == employee:
                count = count + 1
        if count > worst_count:
            worst_count = count
            worst_employee = employee

if worst_employee != "":
    print("Most conflicts         :", worst_employee, "(" + str(worst_count) + " conflict(s))")
    print("Action required        : reschedule", worst_employee, "shifts by at least", MIN_GAP, "hours")
