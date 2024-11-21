import csv

# Define the email data
email_data = [
    'Email',
    'weseGLCIEPTUusDlU@aol.com',
    'uEUSgDKJN@hotmail.com',
    'PLekUVqtWnRVWShep@hotmail.com',
    'BXgWIGaZRv@aol.com',
    'jnacgoqsgJ@upr.edu',
    'hmCdguIbyk@aol.com',
    'iUdkOTYeDMzzwIrytHSh@upr.edu',
    'eEkkQBgmqqQKQ@upr.edu',
    'KKRSFbYPAy@yahoo.com'
]

# Create the CSV file
file_path = "email_data.csv"
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(email_data)

file_path
