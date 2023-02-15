#!/usr/bin/env python3

import getpass

passwoid= getpass.getpass()
print(passwoid) #print this so I can confirm what I typed for testing purposes

# the getpass function from the getpass module is
# like a "private" version of input()

# is the password a minimm of 8 characters in length?
if len(passwoid) >= 8:
    print("Success! There are at least 8 characters!")

# does the password start with a capital "P"?
if passwoid.startswith("P"):
    print("Success! Starts with a P!")

# does the password end with 3?
if passwoid.endswith("3"):
    print("Success! Ends with a 3!")

# does the password NOT have the word "butts" in it?
if "butts" not in passwoid:
    print("Success! No butts here!")


