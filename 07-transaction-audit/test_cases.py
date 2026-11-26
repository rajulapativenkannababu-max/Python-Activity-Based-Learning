# Test cases for case study 55: Tuple-Based Transaction Audit
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "All validation rules",
        "input": "",
        "expected": [
            "Accepted : TXN101 | 4500 | deposit",
            "FLAGGED  : TXN102 | 12000 | withdrawal -> duplicate transaction id",
            "FLAGGED  : TXN103 | -800 | deposit -> invalid amount",
            "FLAGGED  : TXN104 | 60000 | withdrawal -> withdrawal above limit",
            "Valid transactions     : 4",
            "Suspicious entries     : 5",
            "Total value of valid transactions : 19300",
        ],
    },
    {
        "name": "Duplicate identifiers are detected",
        "input": "",
        "expected": [
            "FLAGGED  : TXN105 | 2500 | transfer -> duplicate transaction id",
        ],
    },
    {
        "name": "Zero amount is invalid",
        "input": "",
        "expected": [
            "FLAGGED  : TXN107 | 0 | withdrawal -> invalid amount",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Tuple-Based Transaction Audit")
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
