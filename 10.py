temperature = float(input())
counter = 0
while temperature != 0:
    temperature_1 = temperature
    temperature = float(input())
    if temperature_1 < temperature:
        counter += 1
print(counter)