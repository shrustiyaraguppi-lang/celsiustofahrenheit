import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    if len(sys.argv) > 1:
        celsius = float(sys.argv[1])
    else:
        celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}C = {celsius_to_fahrenheit(celsius)}F")