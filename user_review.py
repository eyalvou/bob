import csv

# Paths to the Excel files
file1 = '/Users/eyalv/Documents/vscod/user_review/bob.csv'  # Replace with the path to your first file
file2 = '/Users/eyalv/Documents/vscod/user_review/jcuserlist.csv'  # Replace with the path to your second file


# Read the Excel files
file1_emails = set()
file2_emails = set()

# Read file1 and extract the 'email' column
with open(file1, 'r') as file1:
    csv_reader = csv.DictReader(file1)
    for row in csv_reader:
        # Ensure 'email' column exists in the row and add it to the set
        if 'Email' in row and row['Email']:
            file1_emails.add(row['Email'].strip())

# Read file2 and extract the 'email' column
with open(file2, 'r') as file2:
    csv_reader = csv.DictReader(file2)
    for row in csv_reader:
        # Ensure 'email' column exists in the row and add it to the set
        if 'Email' in row and row['Email']:
            file2_emails.add(row['Email'].strip())

# Find the emails that are in file1 but not in file2
emails_in_file1_not_in_file2 = file2_emails - file1_emails

# Print the results
if emails_in_file1_not_in_file2:
    print("Emails in file1 but not in file2:")
    for email in emails_in_file1_not_in_file2:
        print(email)
else:
    print("No emails found in file1 that are not in file2.")