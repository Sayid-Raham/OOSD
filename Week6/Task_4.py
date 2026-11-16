# Task 4: Filter valid numeric Celsius readings,
# convert them to Fahrenheit, and round to 1 decimal place.

raw_temps = [22.5, "ERR", 18.0, None, 30.2, "ERR", 0.0]

result = [
    round((temp * 9 / 5) + 32, 1)
    for temp in raw_temps
    if isinstance(temp, (int, float)) and not isinstance(temp, bool)
]

print("Temperatures in Fahrenheit:", result)
