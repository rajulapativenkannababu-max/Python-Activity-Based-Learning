# Test cases for case study 38: ATM Menu-Driven Banking Simulation
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Deposit, withdraw and summary",
        "input": "2600\n1\n2000\n2\n3000\n4\n5\n",
        "expected": [
            "Deposit successful. New balance: 10500",
            "Withdrawal successful. New balance: 7500",
            "1    deposit        2000     10500",
            "2    withdrawal     3000      7500",
            "Transactions : 2",
            "Thank you for banking with us. Closing balance: 7500",
        ],
    },
    {
        "name": "Wrong amount formats are rejected",
        "input": "2600\n2\n250\n2\n50000\n5\n",
        "expected": [
            "REJECTED - enter the amount in multiples of 100",
            "REJECTED - per transaction limit is 20000",
        ],
    },
    {
        "name": "Minimum balance is protected",
        "input": "2600\n2\n8100\n5\n",
        "expected": [
            "REJECTED - insufficient balance, minimum balance 500 must be maintained",
        ],
    },
    {
        "name": "Invalid menu choice",
        "input": "2600\n9\n5\n",
        "expected": [
            "INVALID CHOICE - please enter a number from 1 to 5",
        ],
    },
    {
        "name": "Wrong pin blocks the card",
        "input": "1111\n2222\n3333\n",
        "expected": [
            "Card blocked - three wrong PIN attempts",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for ATM Menu-Driven Banking Simulation")
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
