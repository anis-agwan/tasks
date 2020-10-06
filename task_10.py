# Task 10


# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# akita@securitybrigade.com

# Then, the output of the program should be:

# securitybrigade

# In case of input data being supplied to the question, it should be assumed to be a console input.
def com_name(s):
    idx_at = s.find('@')

    return s[idx_at+1:s.find('.')]

if __name__ == "__main__":
    email = str(input('Enter a valid email address: '))
    print(com_name(email))
    