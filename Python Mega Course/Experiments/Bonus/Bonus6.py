contents = ["File Contents1",
            "File Contents2",
            "File Contents3"]
filenames = ["file1.txt",
             "file2.txt",
             "file3.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../../App_1/files/{filename}", 'w')
    file.write(content)
    file.close()
