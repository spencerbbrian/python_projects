email_address = input("Please enter your email address\n").strip()

username = email_address[:email_address.index('@')]

domain_name = email_address[email_address.index('@')+1:]

print(f"Your username is {username} and your domain name is {domain_name}")