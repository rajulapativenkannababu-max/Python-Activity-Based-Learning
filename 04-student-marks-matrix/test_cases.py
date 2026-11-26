# Test cases for case study 42: Student Marks Matrix Analysis
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Full matrix analysis",
        "input": "",
        "expected": [
            "Sneha              45         38         38         61     182   45.5",
            "Physics     avg = 48.8   min = 38  max = 62  -> LOW AVERAGE - needs attention",
            "Top performer  : Rakesh with 327 marks",
            "Backlog        : Sneha failed in Physics, Chemistry",
            "Class average  : 63.6",
        ],
    },
    {
        "name": "Row totals are correct",
        "input": "",
        "expected": [
            "Anitha             78         55         88         72     293  73.25",
        ],
    },
    {
        "name": "Subject averages are correct",
        "input": "",
        "expected": [
            "English     avg = 70.4   min = 55  max = 95  -> satisfactory",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Student Marks Matrix Analysis")
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
