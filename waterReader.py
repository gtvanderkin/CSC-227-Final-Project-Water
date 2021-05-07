def calcharge(gal, br):
    # This function defines the cost calculation, and returns it
    # There are different rates for 'R'esidential or 'B'usiness rates
    if br == 'R':
        if gal <= 6000:
            return gal * 0.005
        else:
            return (6000 * 0.005) + 0.007 * (gal - 6000)
    else:
        if gal <= 8000:
            return gal * 0.006
        else:
            return (8000 * 0.006) + 0.008 * (gal - 8000)

# Opens the file, and initiates a list to store the contents
myfile = open("water.txt", 'r')
waterlist = []

# copy the file's information to the list
for line in myfile:
    tempid, tempbr, tempgal = line.split(" ")
    waterlist.append([tempid, tempbr, tempgal])

# Calculate and display each entry and the total cost
for x in waterlist:
    print("Account number: " + x[0] + " | Water charge: $" + "{:.2f}".format(calcharge(int(x[2]), x[1])))

myfile.close()
