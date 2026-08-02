import re

with open("emails.txt", "r") as file:
    text = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

with open("extracted_emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Email Addresses Found:\n")

for email in emails:
    print(email)

print("\nSaved to extracted_emails.txt")
