FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    
    fahrenheit = (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
    return fahrenheit

temperature = int(input("Enter the temperature to convert: "))
metric = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if metric == "C":
    conversion = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {conversion}°F")
elif metric == "F":
    conversion = convert_to_celsius(temperature)
    print(f"{temperature}°F is {conversion}°C")
else:
    print("Invalid input")