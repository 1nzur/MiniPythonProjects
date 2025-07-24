fname = input("Enter the name of file: ")
try:
    xfile = open(fname)
except:
    print("Invalid file name")
    exit()
print("Successfully opened the file", fname)
c = 0
w = input("Enter the word you want to count: ")
w = w.lower()
for line in xfile:
    line = line.lower()
    sword = line.split()
    for word in sword:
        if word == w:
            c = c+1

print("The word you've entered has been repeated", c, "times")
