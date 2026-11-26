# Test cases for case study 37: Nested Loop Calendar Generator
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "November 2026 style month",
        "input": "11\n30\n6\n",
        "expected": [
            "November  -  30 days, starts on Sat",
            "                             1    2",
            "   24   25   26   27   28   29   30",
            "Working days : 20",
            "Weekend days : 10",
        ],
    },
    {
        "name": "Weekday check with 31 days",
        "input": "1\n31\n4\n",
        "expected": [
            "January  -  31 days, starts on Thu",
            "Working days : 22",
        ],
    },
    {
        "name": "Invalid month number",
        "input": "13\n30\n1\n",
        "expected": [
            "INVALID MONTH - please enter a number between 1 and 12",
        ],
    },
    {
        "name": "Invalid month length",
        "input": "2\n25\n3\n",
        "expected": [
            "INVALID MONTH LENGTH - a month can have only 28 to 31 days",
        ],
    },
    {
        "name": "Invalid weekday",
        "input": "5\n31\n9\n",
        "expected": [
            "INVALID WEEKDAY - please enter 1 for Monday up to 7 for Sunday",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Nested Loop Calendar Generator")
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
