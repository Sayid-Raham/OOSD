# Task 6: Calculate averages for every contiguous window of size k.

prices = [100, 102, 104, 103, 105, 110]
k = 3

result = [
    (i, round(sum(prices[i:i + k]) / k, 2))
    for i in range(len(prices) - k + 1)
]

print("Window averages:", result)
