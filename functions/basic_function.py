def is_valid_email(email):
    """Check if the provided email is valid."""
    if '@' in email and '.' in email and email.count('@') == 1 and email.index('@') < email.rindex('.'):
        return True
    return False


input_email = input("Enter your email: ")
if is_valid_email(input_email):
    print("The email is valid.")
else:
    print("The email is invalid.")