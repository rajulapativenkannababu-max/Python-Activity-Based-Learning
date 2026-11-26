# Case Study 42: Student Marks Matrix Analysis
# Syllabus used: variables, operators, conditional statements, loops, strings, lists, nested lists

print("STUDENT MARKS MATRIX ANALYSIS")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 62)

students = ["Anitha", "Rakesh", "Sneha", "Vikram", "Meena"]
subjects = ["Maths", "Physics", "Chemistry", "English"]

# nested list - one inner list of marks for each student
marks = [
    [78, 55, 88, 72],
    [91, 62, 79, 95],
    [45, 38, 38, 61],
    [67, 48, 70, 69],
    [58, 41, 62, 55],
]
PASS_MARK = 40

print("Marks matrix (rows = students, columns = subjects)")
header = "Student".ljust(10)
for subject in subjects:
    header = header + subject.rjust(11)
header = header + "   Total   Avg"
print(header)
print("-" * 62)

row_totals = []
for i in range(len(students)):
    row_total = 0
    for j in range(len(subjects)):
        row_total = row_total + marks[i][j]
    row_totals.append(row_total)

    line = students[i].ljust(10)
    for j in range(len(subjects)):
        line = line + str(marks[i][j]).rjust(11)
    line = line + str(row_total).rjust(8)
    line = line + str(round(row_total / len(subjects), 2)).rjust(7)
    print(line)

print("-" * 62)

# column-wise (subject-wise) statistics
print("Subject-wise analysis")
for j in range(len(subjects)):
    column_total = 0
    lowest = marks[0][j]
    highest = marks[0][j]
    for i in range(len(marks)):
        column_total = column_total + marks[i][j]
        if marks[i][j] < lowest:
            lowest = marks[i][j]
        if marks[i][j] > highest:
            highest = marks[i][j]
    average = round(column_total / len(students), 2)
    if average < 60:
        remark = "LOW AVERAGE - needs attention"
    else:
        remark = "satisfactory"
    print(" ", subjects[j].ljust(11), "avg =", str(average).ljust(6),
          "min =", str(lowest).ljust(3), "max =", str(highest).ljust(3), "->", remark)

print("-" * 62)

# top performer
top_index = 0
for i in range(1, len(students)):
    if row_totals[i] > row_totals[top_index]:
        top_index = i
print("Top performer  :", students[top_index], "with", row_totals[top_index], "marks")

# students with a failed subject
for i in range(len(students)):
    failed = ""
    for j in range(len(subjects)):
        if marks[i][j] < PASS_MARK:
            if failed != "":
                failed = failed + ", "
            failed = failed + subjects[j]
    if failed != "":
        print("Backlog        :", students[i], "failed in", failed)

# overall class average
class_total = 0
for total in row_totals:
    class_total = class_total + total
print("Class average  :", round(class_total / (len(students) * len(subjects)), 2))
