# Multiplication Table Generator (Python)

Veda Technology Python Internship — Level 1, Task 6

A Python program that accepts a number and generates its multiplication table up to a limit chosen by the user.

## Objective
Practice loops and formatted output.

## Tools
- Python 3 (no external libraries)

## Features
- Takes the number and the limit (range) from the user
- Uses a `for` loop to print each line of the table
- Output is formatted clearly as `number x i = result`
- Handles invalid input: letters stop the program with a clear message
- Rejects a limit below 1

## How to Run
```bash
python multiplication_table.py
```

## Approach
- The number and the limit are read with `int(input())` inside a `try/except ValueError` block. If the user enters anything other than whole numbers, a message is shown and the program stops with `exit()`.
- An `if limit < 1` check stops the program with a message if the limit is zero or negative.
- `for i in range(1, limit + 1)` goes from 1 to the limit, and each line is printed with an f-string: `{number} x {i} = {result}`.
- Dashed lines (`"-" * 30`) are printed above and below the table to keep the output clean.

## Sample Output (three different numbers)

**Number 5, limit 10**
```
===== MULTIPLICATION TABLE =====
Enter a number: 5
Enter the limit: 10

Multiplication Table of 5
------------------------------
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
------------------------------
```

**Number 12, limit 12**
```
===== MULTIPLICATION TABLE =====
Enter a number: 12
Enter the limit: 12

Multiplication Table of 12
------------------------------
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
12 x 11 = 132
12 x 12 = 144
------------------------------
```

**Number 7, limit 15**
```
===== MULTIPLICATION TABLE =====
Enter a number: 7
Enter the limit: 15

Multiplication Table of 7
------------------------------
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84
7 x 13 = 91
7 x 14 = 98
7 x 15 = 105
------------------------------
```

## Invalid Input Handling

**Letters instead of a number**
```
===== MULTIPLICATION TABLE =====
Enter a number: abc
Please enter whole numbers only
```

**Limit below 1**
```
===== MULTIPLICATION TABLE =====
Enter a number: 5
Enter the limit: 0
Limit must be at least 1
```

## Interview Questions

**1. When would you use a for loop?**
When the number of repetitions is known in advance, or when going through the items of a sequence such as a list, string or `range()`. In this program the table has a fixed number of lines (1 to the limit), so a `for` loop is the natural choice. A `while` loop is better when we do not know how many times it will run.

**2. What does range() return?**
In Python 3, `range()` returns a `range` object, which is an immutable sequence of numbers created one at a time instead of storing them all in memory. It can be converted to a list with `list(range(5))`, which gives `[0, 1, 2, 3, 4]`.

**3. What is the difference between range(5) and range(1, 5)?**
`range(5)` starts at 0 and stops before 5, giving 0, 1, 2, 3, 4. `range(1, 5)` starts at 1 and stops before 5, giving 1, 2, 3, 4. The stop value is never included. That is why this program uses `range(1, limit + 1)` to include the limit.

## Outcome
The program generates a correctly formatted multiplication table for any number and limit, and handles invalid input safely.