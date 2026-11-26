# Case Study 55: Tuple-Based Transaction Audit
# Syllabus used: variables, operators, conditional statements, loops, strings, lists, tuples,
#               tuple operations and unpacking

print("TUPLE-BASED TRANSACTION AUDIT")
print("Student : Rajulapati Venkanna Babu")
print("Roll No : 26000709")
print("-" * 60)

# each transaction is a tuple: (transaction id, amount, transaction type)
transactions = (
    ("TXN101", 4500, "deposit"),
    ("TXN102", 12000, "withdrawal"),
    ("TXN102", 12000, "withdrawal"),
    ("TXN103", -800, "deposit"),
    ("TXN104", 60000, "withdrawal"),
    ("TXN105", 2500, "transfer"),
    ("TXN105", 2500, "transfer"),
    ("TXN106", 300, "deposit"),
    ("TXN107", 0, "withdrawal"),
)

MAX_WITHDRAWAL = 50000     # single withdrawal limit fixed by the bank
FLAG_LIMIT = 30000         # any transaction above this amount is reported

print("Transaction log")
for txn_id, amount, txn_type in transactions:          # tuple unpacking
    print("  " + txn_id, str(amount).rjust(7), " " + txn_type)
print("-" * 60)

seen_ids = []
suspicious = []            # suspicious entries stored as tuples
valid_count = 0
valid_total = 0

for txn_id, amount, txn_type in transactions:
    reason = ""

    if amount <= 0:
        reason = "invalid amount"
    elif txn_type != "deposit" and txn_type != "withdrawal" and txn_type != "transfer":
        reason = "unknown transaction type"
    elif txn_type == "withdrawal" and amount > MAX_WITHDRAWAL:
        reason = "withdrawal above limit"
    elif amount > FLAG_LIMIT:
        reason = "high value transaction"

    if txn_id in seen_ids:
        if reason == "":
            reason = "duplicate transaction id"
        else:
            reason = reason + " + duplicate transaction id"

    seen_ids.append(txn_id)

    if reason == "":
        valid_count = valid_count + 1
        valid_total = valid_total + amount
        print("Accepted :", txn_id, "|", amount, "|", txn_type)
    else:
        suspicious.append((txn_id, amount, txn_type, reason))
        print("FLAGGED  :", txn_id, "|", amount, "|", txn_type, "->", reason)

print("-" * 60)
print("Valid transactions     :", valid_count)
print("Suspicious entries     :", len(suspicious))

if len(suspicious) > 0:
    print()
    print("Suspicious transaction report")
    for txn_id, amount, txn_type, reason in suspicious:      # tuple unpacking
        print("  " + txn_id.ljust(8), str(amount).rjust(7), " " + txn_type.ljust(11), "->", reason)

print()
print("Total value of valid transactions :", valid_total)
print("Audit completed for", len(transactions), "transactions")
