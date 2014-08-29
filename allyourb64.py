"""
Reads in a newline-delimited userlist file and passwords file and creates a
formatted output (user:password) file mapping each user to all passwords,
base-64-encoded.

"""

import sys
import base64


def main():
    """
    This ingests the input files (a newline-delimited userlist file and a
    newline-delimited passwords-list file) and creates a formatted output file
    of matching each user with all passwords.

    The userlist file is assumed to be the first command-line argumnet; the
    passwords file the second; and the output file the third.

    """
    with open(sys.argv[1], 'r') as f:
        userlist = [line.strip() for line in f]
    with open(sys.argv[2], 'r') as f:
        pwlist = [line.strip() for line in f]
    with open(sys.argv[3], 'w') as f:
        for user in userlist:
            for pw in pwlist:
                f.write(base64.b64encode('%s:%s' % (user, pw)) + '\n')


# If called on the command-line as a script, launch main function.
if __name__ == "__main__":
    main()
