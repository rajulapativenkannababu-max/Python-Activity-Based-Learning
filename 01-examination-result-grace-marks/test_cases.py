# Test cases for case study 11: Examination Result and Grace-Mark Validation
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Normal case with grace marks",
        "input": "",
        "expected": [
            "Maths         72    72  PASS",
            "Physics       33    35  PASS WITH GRACE (+2)",
            "Chemistry     28    28  FAIL",
            "Percentage      : 58.0 %",
            "Grace subjects  : 1 (total grace marks = 2)",
            "Failed subjects : 1",
            "Classification  : FAIL - CLEAR THE FAILED SUBJECT(S)",
        ],
    },
    {
        "name": "Grace limit not exceeded check",
        "input": "",
        "expected": [
            "Grace subjects  : 1",
            "PASS WITH GRACE (+2)",
        ],
    },
    {
        "name": "Total of final marks",
        "input": "",
        "expected": [
            "Total marks     : 290 / 500",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Examination Result and Grace-Mark Validation")
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
