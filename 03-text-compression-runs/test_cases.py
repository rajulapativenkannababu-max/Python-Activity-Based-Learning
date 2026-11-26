# Test cases for case study 35: Text Compression Using Character Runs
# Each test runs solution.py with the given input and checks the expected output text.

import subprocess
import sys

SOLUTION = "solution.py"

tests = [
    {
        "name": "Repeated characters",
        "input": "aaabbbcccd\n",
        "expected": [
            "Encoded text    : a3b3c3d1",
            "Result          : encoding is BENEFICIAL",
        ],
    },
    {
        "name": "Single character run",
        "input": "aaaaa\n",
        "expected": [
            "Encoded text    : a5",
            "Result          : encoding is BENEFICIAL",
        ],
    },
    {
        "name": "Encoding not beneficial",
        "input": "abcde\n",
        "expected": [
            "Encoded text    : a1b1c1d1e1",
            "Result          : encoding is NOT BENEFICIAL",
        ],
    },
    {
        "name": "Empty text is rejected",
        "input": "\n",
        "expected": [
            "INVALID INPUT - the text is empty",
        ],
    },
    {
        "name": "Mixed case is treated as different characters",
        "input": "aAbB\n",
        "expected": [
            "Encoded text    : a1A1b1B1",
        ],
    },
]

passed = 0
failed = 0

print("Running", len(tests), "test cases for Text Compression Using Character Runs")
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
