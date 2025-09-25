'''

°F=(°C×1.8)+32

'''

def convert(C):
    F = (C * 1.8)+32
    print(f"Temperature in fahrenheit will be {F}")

C = int(input("Enter temp in celsius to change in fahrenheit:"))

convert(C)