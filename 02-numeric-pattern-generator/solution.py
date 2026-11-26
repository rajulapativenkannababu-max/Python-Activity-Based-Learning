# Case Study 27: Advanced Numeric Pattern Generator
# Syllabus used: variables, operators, conditional statements, loops, pattern generation

print("ADVANCED NUMERIC PATTERN GENERATOR")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 46)

n = int(input("Enter the size of the pattern (odd number, 3 to 15): "))

if n < 3 or n > 15:
    print("INVALID SIZE - the size must be between 3 and 15")
elif n % 2 == 0:
    print("INVALID SIZE - an even number cannot form a symmetric diamond")
else:
    middle = n // 2 + 1

    print()
    print("1) Hollow diamond of numbers")
    for row in range(1, n + 1):
        if row <= middle:
            stars = row
        else:
            stars = n - row + 1

        line = ""
        spaces = middle - stars
        for s in range(spaces):
            line = line + "   "
        for col in range(1, stars + 1):
            if col == 1 or col == stars:
                line = line + str(stars).rjust(2) + " "
            else:
                line = line + "   "
        print(line)

    print()
    print("2) Number pyramid")
    for row in range(1, middle + 1):
        line = ""
        for s in range(middle - row):
            line = line + "  "
        for col in range(1, row + 1):
            line = line + str(col) + " "
        for col in range(row - 1, 0, -1):
            line = line + str(col) + " "
        print(line)

    print()
    print("3) Reverse number triangle")
    for row in range(middle, 0, -1):
        line = ""
        for col in range(1, row + 1):
            line = line + str(row) + " "
        print(line)

    print()
    print("Pattern generated successfully for size", n)
