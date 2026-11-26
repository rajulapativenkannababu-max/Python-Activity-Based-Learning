# Test cases for case study 27: Advanced Numeric Pattern Generator
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Valid odd size 7",
        "input": "7\n",
        "expected": [
            "1) Hollow diamond of numbers",
            " 4        4",
            "1 2 3 4 3 2 1",
            "Pattern generated successfully for size 7",
        ],
    },
    {
        "name": "Even size is rejected",
        "input": "6\n",
        "expected": [
            "INVALID SIZE - an even number cannot form a symmetric diamond",
        ],
    },
    {
        "name": "Size below the lower limit",
        "input": "2\n",
        "expected": [
            "INVALID SIZE - the size must be between 3 and 15",
        ],
    },
    {
        "name": "Size above the upper limit",
        "input": "21\n",
        "expected": [
            "INVALID SIZE - the size must be between 3 and 15",
        ],
    },
    {
        "name": "Smallest valid size 3",
        "input": "3\n",
        "expected": [
            "1) Hollow diamond of numbers",
            "Pattern generated successfully for size 3",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Advanced Numeric Pattern Generator")
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
