# Case Study 35: Text Compression Using Character Runs
# Syllabus used: variables, operators, conditional statements, loops, strings

print("TEXT COMPRESSION USING CHARACTER RUNS")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 46)

text = input("Enter the text to be compressed: ")

if len(text) == 0:
    print("INVALID INPUT - the text is empty")
else:
    encoded = ""
    run_char = text[0]
    run_count = 1

    for i in range(1, len(text)):
        if text[i] == run_char:
            run_count = run_count + 1
        else:
            encoded = encoded + run_char + str(run_count)
            run_char = text[i]
            run_count = 1
    encoded = encoded + run_char + str(run_count)     # last run is added after the loop

    print()
    print("Original text   :", text)
    print("Encoded text    :", encoded)
    print("Original length :", len(text))
    print("Encoded length  :", len(encoded))

    saved = len(text) - len(encoded)
    if saved > 0:
        ratio = round(len(text) / len(encoded), 2)
        print("Result          : encoding is BENEFICIAL")
        print("Space saved     :", saved, "characters (" + str(ratio) + " : 1 compression)")
    elif saved == 0:
        print("Result          : encoding is NEUTRAL - same length as the original")
    else:
        print("Result          : encoding is NOT BENEFICIAL - original text is shorter")
