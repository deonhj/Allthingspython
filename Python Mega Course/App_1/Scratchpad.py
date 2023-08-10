def strength(password):
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

    if all(result.values()):
        test = "Strong password!"
    else:
        test = "Weak sauce password"
    return test
