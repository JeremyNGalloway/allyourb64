# allyourb64
Converts a file *Line By Line* into b64 encoded strings

This ingests the input files (a newline-delimited userlist file and a
newline-delimited passwords-list file) and creates a formatted output file
of matching each user with all passwords.
The userlist file is assumed to be the first command-line argumnet; the
passwords file the second; and the output file the third.

python b64.py users.txt passes.txt b64BASIC.out
