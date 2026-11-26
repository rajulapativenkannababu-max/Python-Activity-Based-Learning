# Case Study 58: Library Borrowing and Fine Reconciliation
# Syllabus used: variables, operators, conditional statements, loops, strings, lists, tuples,
#               tuple operations and unpacking

print("LIBRARY BORROWING AND FINE RECONCILIATION")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 64)

FREE_DAYS = 14          # books may be kept for 14 days without fine
FINE_SLAB_1 = 2         # rupees per day for days 1 to 7 after the due date
FINE_SLAB_2 = 5         # rupees per day for days 8 to 15 after the due date
FINE_SLAB_3 = 10        # rupees per day after that
MAX_FINE = 300          # fine is capped per book

# each record is a tuple: (book id, title, borrower, days kept)
records = (
    ("B101", "Let Us C", "Anitha", 10),
    ("B102", "Python Basics", "Rakesh", 21),
    ("B103", "Data Structures", "Sneha", 34),
    ("B104", "Operating Systems", "Vikram", 14),
    ("B105", "Discrete Maths", "Meena", 45),
    ("B106", "Computer Networks", "Anitha", 3),
)

print("Borrowing register")
for book_id, title, borrower, days in records:          # tuple unpacking
    print("  " + book_id, "|", title.ljust(20), "|", borrower.ljust(8), "|", str(days).rjust(3), "days")
print("-" * 64)

total_fine = 0
overdue_count = 0
fine_report = []
borrower_names = []
borrower_fines = []

for book_id, title, borrower, days in records:
    if days <= FREE_DAYS:
        fine = 0
        status = "ON TIME"
        late = 0
    else:
        late = days - FREE_DAYS
        if late <= 7:
            fine = late * FINE_SLAB_1
        elif late <= 15:
            fine = 7 * FINE_SLAB_1 + (late - 7) * FINE_SLAB_2
        else:
            fine = 7 * FINE_SLAB_1 + 8 * FINE_SLAB_2 + (late - 15) * FINE_SLAB_3

        if fine > MAX_FINE:
            fine = MAX_FINE
        status = "OVERDUE (" + str(late) + " days late)"
        overdue_count = overdue_count + 1

    total_fine = total_fine + fine
    fine_report.append((book_id, title, borrower, days, fine, status))

    if borrower in borrower_names:
        position = borrower_names.index(borrower)
        borrower_fines[position] = borrower_fines[position] + fine
    else:
        borrower_names.append(borrower)
        borrower_fines.append(fine)

print("Book  Title                Borrower   Days  Fine   Status")
print("-" * 64)
for book_id, title, borrower, days, fine, status in fine_report:      # tuple unpacking
    print(book_id.ljust(6), title.ljust(20), borrower.ljust(10),
          str(days).rjust(3), str(fine).rjust(5), " " + status)

print("-" * 64)
print("Overdue books        :", overdue_count, "out of", len(records))
print("Total fine collected :", total_fine, "rupees")

print()
print("Borrower-wise fine summary")
for i in range(len(borrower_names)):
    if borrower_fines[i] > 0:
        remark = "fine pending"
    else:
        remark = "no dues"
    print("  " + borrower_names[i].ljust(10), str(borrower_fines[i]).rjust(5), " " + remark)

# highest fine paying borrower
if len(borrower_names) > 0:
    top = 0
    for i in range(1, len(borrower_names)):
        if borrower_fines[i] > borrower_fines[top]:
            top = i
    print()
    print("Highest fine      :", borrower_names[top], "(" + str(borrower_fines[top]) + " rupees)")
    print("Reconciliation done for", len(records), "borrowed books")
