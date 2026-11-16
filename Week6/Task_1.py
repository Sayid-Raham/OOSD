# Task 1: Remove first two and last two readings,
# then return the remaining readings in reverse order.

times = [120, 45, 32, 28, 41, 39, 35, 210]

# Single slice expression
result = times[-3:1:-1]

print("Original readings:", times)
print("Remaining readings in reverse order:", result)
