# Test cases for case study 100: Comprehensive Smart Campus Management Simulation
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Student and attendance report",
        "input": "1\n2\n7\n",
        "expected": [
            "26000709   Rajulapati Venkanna Babu     92     78",
            "NOT ELIGIBLE - short by 7%",
            "Attendance eligible     : 2 out of 4",
        ],
    },
    {
        "name": "Nested list marks analysis",
        "input": "3\n7\n",
        "expected": [
            "Average in Maths        = 54.75",
            "Students with a backlog : 2",
            "Sneha Sharma                        34          41          27  FAIL in 2 subject(s)",
        ],
    },
    {
        "name": "Duplicate event registration",
        "input": "4\n7\n",
        "expected": [
            "DUPLICATE ENTRY REJECTED",
            "Total valid registrations : 3",
        ],
    },
    {
        "name": "Resource allocation and shortfall",
        "input": "5\nLaptop\n3\n5\nProjector\n6\n7\n",
        "expected": [
            "ALLOCATED 3 unit(s) of Laptop",
            "Remaining : 3 unit(s)",
            "PARTIAL - only 4 unit(s) of Projector available",
            "Shortfall : 2 unit(s)",
        ],
    },
    {
        "name": "Invalid resource name",
        "input": "5\nChair\n2\n7\n",
        "expected": [
            "INVALID - 'Chair' is not a campus resource",
        ],
    },
    {
        "name": "Summary report",
        "input": "6\n7\n",
        "expected": [
            "Average attendance      : 74.0%",
            "Best overall marks      : Rajulapati Venkanna Babu (78)",
            "Attendance warning      : Anitha Rao, Sneha Sharma",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Comprehensive Smart Campus Management Simulation")
print("-" * 56)

for test in tests:
    result = subprocess.run(
        [sys.executable, SOLUTION],
        input=test["input"],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    ok = True
    missing = []
    for expected_line in test["expected"]:
        if expected_line not in output:
            ok = False
            missing.append(expected_line)

    if ok:
        passed = passed + 1
        print("PASS :", test["name"])
    else:
        failed = failed + 1
        print("FAIL :", test["name"])
        for line in missing:
            print("       missing ->", line)

print("-" * 56)
print("Total tests :", len(tests))
print("Passed      :", passed)
print("Failed      :", failed)

if failed == 0:
    print("RESULT : all test cases passed")
else:
    print("RESULT : some test cases failed")
    sys.exit(1)
