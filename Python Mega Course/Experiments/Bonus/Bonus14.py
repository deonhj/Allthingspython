from Converters14 import convert
from Parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print("Rider is too small.")
else:
    print("Rider can go on the ride.")
