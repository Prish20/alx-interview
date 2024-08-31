# 0x03. Log Parsing

## Task 0: Log Parsing

This task involves writing a Python script that reads stdin line by line and computes metrics based on the input format provided.

**File:** `0-stats.py`

**Input Format:**

**Functionality:**

- The script reads lines from stdin.
- It computes and prints the total file size and the number of occurrences of each status code after every 10 lines or upon a keyboard interrupt (CTRL + C).
- The status codes are printed in ascending order.

**Usage:**

You can run the script with:

```bash
./0-generator.py | ./0-stats.py
