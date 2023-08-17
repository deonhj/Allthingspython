feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3028 + inches * 0.0254
    return meters


result = convert(feet_inches)

if result < 1:
    print("Rider is too small.")
else:
    print("Rider can go on the ride.")