# Case Study 11: Examination Result and Grace-Mark Validation
# Syllabus used: variables, operators, conditional statements, loops, strings, lists, tuples

PASS_MARK = 35
MAX_MARK = 100
GRACE_LIMIT = 5          # maximum grace marks that can be given in one subject
MAX_GRACE_SUBJECTS = 2   # maximum number of subjects that can receive grace

subjects = ["Maths", "Physics", "Chemistry", "English", "Programming"]
marks = (72, 33, 28, 64, 91)      # raw marks of one student stored in a tuple

print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 52)

fail_count = 0
grace_used = 0
grace_marks = 0
total = 0
report = []

for i in range(len(subjects)):
    subject = subjects[i]
    raw = marks[i]

    if raw < 0 or raw > MAX_MARK:
        final = 0
        status = "INVALID MARK"
        fail_count = fail_count + 1
    elif raw >= PASS_MARK:
        final = raw
        status = "PASS"
        total = total + final
    else:
        shortfall = PASS_MARK - raw
        if shortfall <= GRACE_LIMIT and grace_used < MAX_GRACE_SUBJECTS:
            final = PASS_MARK          # grace never pushes a mark above 100
            grace_used = grace_used + 1
            grace_marks = grace_marks + shortfall
            status = "PASS WITH GRACE (+" + str(shortfall) + ")"
            total = total + final
        else:
            final = raw
            status = "FAIL"
            fail_count = fail_count + 1
            total = total + final

    report.append((subject, raw, final, status))

print("Subject      Raw  Final  Status")
print("-" * 52)
for subject, raw, final, status in report:        # tuple unpacking inside for loop
    print(subject.ljust(12), str(raw).rjust(3), str(final).rjust(5), " " + status)
print("-" * 52)

percentage = round(total / len(subjects), 2)

if fail_count == 0 and grace_used == 0:
    classification = "FIRST CLASS - NO GRACE NEEDED"
elif fail_count == 0:
    classification = "PASS - GRACE MARKS APPLIED"
else:
    classification = "FAIL - CLEAR THE FAILED SUBJECT(S)"

print("Total marks     :", total, "/", MAX_MARK * len(subjects))
print("Percentage      :", percentage, "%")
print("Grace subjects  :", str(grace_used) + " (total grace marks = " + str(grace_marks) + ")")
print("Failed subjects :", fail_count)
print("Classification  :", classification)
