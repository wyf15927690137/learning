
# Import re module
import re

# The input string to search within
text = "Contact SparkByExamples at sparkbyexamples@gmail.com or sparkbyexamples@example.com for further information."

# Find all email addresses in the text using the regular expression pattern
# the pattern matches valid email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

# Print the list of email addresses found
print(emails)

# A string variable text is defined, which contains the text to search within. The re.findall() method is used to find all occurrences of a pattern in the text string. The pattern r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' is a regular expression pattern that matches valid email addresses.

# It looks for sequences of characters that start with a word boundary (\b), followed by a combination of alphanumeric characters, dots, underscores, percentage signs, plus signs, or hyphens ([A-Za-z0-9._%+-]+), followed by the @ symbol, then another sequence of alphanumeric characters, dots, or hyphens ([A-Za-z0-9.-]+), and finally, a period followed by at least two letters (\.[A-Za-z]{2,}). The final word boundary (\b) ensures that the match ends at a word boundary.