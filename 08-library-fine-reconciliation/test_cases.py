# Test cases for case study 58: Library Borrowing and Fine Reconciliation
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Slab wise fine calculation",
        "input": "",
        "expected": [
            "B102   Python Basics        Rakesh      21    14  OVERDUE (7 days late)",
            "B103   Data Structures      Sneha       34   104  OVERDUE (20 days late)",
            "B105   Discrete Maths       Meena       45   214  OVERDUE (31 days late)",
            "Overdue books        : 3 out of 6",
            "Total fine collected : 332 rupees",
        ],
    },
    {
        "name": "Books returned within 14 days have no fine",
        "input": "",
        "expected": [
            "B104   Operating Systems    Vikram      14     0  ON TIME",
        ],
    },
    {
        "name": "Borrower wise summary",
        "input": "",
        "expected": [
            "Highest fine      : Meena (214 rupees)",
            "Anitha         0  no dues",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Library Borrowing and Fine Reconciliation")
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
