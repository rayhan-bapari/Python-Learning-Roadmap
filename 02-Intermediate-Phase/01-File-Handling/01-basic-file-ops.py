# File Handling Practice
# Reading and writing files

# Write to file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

# Read from file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# TODO: Practice with CSV files, JSON files
