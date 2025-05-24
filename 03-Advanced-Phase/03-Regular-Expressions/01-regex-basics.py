# Regular Expressions Practice
import re

text = "Contact us at email@example.com or phone 123-456-7890"

# Find email
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# TODO: Practice more regex patterns
