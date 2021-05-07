def isnum(instr):
    # A simple function that determines whether a string is an integer.
    # It attempts to explicitly cast the string to a number in a try/except block:
    # If it succeeds, it's apparently an integer, returning True.
    # If it would produce an error, it catches that to return False.

    try:
        int(instr)
        return True
    except ValueError:
        return False

# Initialize a loop condition to "Y" for 'yes,' and a blank string.
# Create/open a text file to write/overwrite to.

goon = "Y"
myfile = open('water.txt', 'w')
s = ""

# Start the loop!
while goon == "Y":

    # Take user input for the account number, account type, and amount of water used
    # Input verification does its best to make sure
    s = ""
    verify = input("Enter account number: ")
    while not isnum(verify):
        print("Please enter an integer.")
        verify = input("Enter account number: ")
    s = verify
    verify = input("Enter R for residential, B for business: ").upper()
    while verify != 'R' and verify != 'B':
        print("Invalid character.")
        verify = input("Enter R for residential, B for business: ").upper()
    s += " " + verify
    verify = input("Enter gallons used: ")
    while not isnum(verify):
        print("Please enter an integer.")
        verify = input("Enter gallons used: ")
    s += " " + verify

    # Writes the information to a file, and allows the user to continue the loop, or end it
    myfile.write(s)
    goon = input("Go on? Y for yes. ").upper()
    myfile.write('\n')

myfile.close()
