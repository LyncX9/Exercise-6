temperature = float(input("Enter the temperature in Celsius: "))

if temperature < -10:
    print("Freezing")
elif -10 <= temperature < 0:
    print("Very Cold")
elif 0 <= temperature < 10:
    print("Cold")
elif 10 <= temperature < 20:
    print("Moderate")
elif 20 <= temperature < 30:
    print("Hot")
else:
    print("Very Hot")