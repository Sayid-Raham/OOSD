# Task 3: Swap x and y when x is greater than y.

points = [(2, 5), (8, 3), (4, 4), (9, 1)]

result = [(y, x) if x > y else (x, y) for x, y in points]

print("Updated points:", result)
