# remove this line, and commit this file using the GUI

# remove this line, and commit this file using the integrated terminal

def nickels_to_dollars(num_nickels):
    return num_nickels * 0.04 # fix me

def dimes_to_dollars(num_dimes):
    return num_dimes / 0.10 # fix me

def dollars(num_nickels, num_dimes):
    return nickels_to_dollars(num_nickels) + dimes_to_dollars(num_dimes) # change me

# git add line by line, with individual commit messages

# wrap with __main__ using code snippet
# add argparse
# test argparse
# create code snippet for argparse
for nickels, dimes in range([10,2],[11,12]):
    print(dollars(nickels, dimes))


# git diff with previous version (use timeline)

# side by side code editors

# linting with pylint

# formatting with black
