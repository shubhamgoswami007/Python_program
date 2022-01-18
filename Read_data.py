

def readdata(name):
    print(name.read())

print("rajkot file data: \n-----------------")
file1 = open("RAJKOT.txt", "r")
readdata(file1)

print("\nMumbai file data: \n-----------------")
file1 = open("MUMBAI.txt", "r")
readdata(file1)

print("\nJamnager file data: \n-----------------")
file1 = open("JAMNAGAR.txt", "r")
readdata(file1)

print("\nAhmedabad file data: \n-----------------")
file1 = open("AHMEDABAD.txt", "r")
readdata(file1)

file1.close()
