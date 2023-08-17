password = input("enter new password: ")
result = {}
if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result["Upper"] = upper

if all(result.values()):  # All returns True if all values in the list/dictionary are True
    print("Strong password!")
else:
    print("Weak sauce password!")