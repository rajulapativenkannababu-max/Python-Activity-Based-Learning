# Case Study 37: Nested Loop Calendar Generator
# Syllabus used: variables, operators, conditional statements, loops, strings, pattern generation

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("NESTED LOOP CALENDAR GENERATOR")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 46)

month = int(input("Enter month number (1 to 12): "))
total_days = int(input("Enter number of days in the month (28 to 31): "))
start_day = int(input("Enter starting weekday (1 = Monday ... 7 = Sunday): "))

if month < 1 or month > 12:
    print("INVALID MONTH - please enter a number between 1 and 12")
elif total_days < 28 or total_days > 31:
    print("INVALID MONTH LENGTH - a month can have only 28 to 31 days")
elif start_day < 1 or start_day > 7:
    print("INVALID WEEKDAY - please enter 1 for Monday up to 7 for Sunday")
else:
    print()
    print(MONTHS[month - 1] + "  -  " + str(total_days) + " days, starts on " + DAYS[start_day - 1])
    print("-" * 46)

    header = ""
    for day_name in DAYS:
        header = header + day_name.rjust(5)
    print(header)

    # outer loop = weeks, inner loop = the seven weekdays of a week
    date = 1
    for week in range(6):
        line = ""
        for weekday in range(1, 8):
            if week == 0 and weekday < start_day:
                line = line + "     "          # blank cells before the 1st date
            elif date <= total_days:
                line = line + str(date).rjust(5)
                date = date + 1
            else:
                line = line + "     "
        if line.strip() != "":
            print(line)
        if date > total_days:
            break

    print("-" * 46)

    # weekend count for the month
    weekends = 0
    for date in range(1, total_days + 1):
        position = (start_day - 1 + date - 1) % 7
        if position == 5 or position == 6:
            weekends = weekends + 1

    print("Working days :", total_days - weekends)
    print("Weekend days :", weekends)
    print("Calendar generated successfully for", MONTHS[month - 1])
