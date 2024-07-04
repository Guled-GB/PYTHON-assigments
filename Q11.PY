string = "Coding For All"

try:
    index = string.index("Coding")
    print("Substring 'Coding' found at index:", index)
except ValueError:
    print("Substring 'Coding' not found")
