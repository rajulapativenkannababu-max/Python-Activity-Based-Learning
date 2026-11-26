# Test cases for case study 48: Tuple-Based Employee Shift Conflict Detection
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Overlap and rest gap detection",
        "input": "",
        "expected": [
            "Conflict : E101 on Monday -> INSUFFICIENT REST (1 h)",
            "Conflict : E104 on Wednesday -> OVERLAP",
            "Total conflicts found : 2",
        ],
    },
    {
        "name": "Clean employees are listed",
        "input": "",
        "expected": [
            "Employees without any conflict : ['E102', 'E103', 'E105']",
        ],
    },
    {
        "name": "Employee with most conflicts",
        "input": "",
        "expected": [
            "Most conflicts         : E101 (1 conflict(s))",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Tuple-Based Employee Shift Conflict Detection")
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
