filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [name.replace('.', '-') + '.txt' for name in filenames]
print(filenames)
