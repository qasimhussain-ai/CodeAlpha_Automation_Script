import re

# Read the text file
with open("data.txt", "r") as f:
    text = f.read()

# Regex to extract emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save to file
with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted successfully and saved to emails.txt")
