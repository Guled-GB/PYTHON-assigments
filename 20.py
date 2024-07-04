# Define the string
text = "Coding For All"

# Split the string into words
words = text.split()

# Take the first letter of each word and combine them to form the acronym
acronym = ''.join(word[0] for word in words).upper()

# Print the acronym
print(acronym)
