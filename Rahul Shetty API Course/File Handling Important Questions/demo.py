file = open('Rahul Shetty API Course\\File Handling Important Questions\\abc.txt')
lines = [line.strip() for line in file.readlines()]
# print list of lines
print(lines)

# printing line by line
# No output because we read all lines above
for line in file.readlines():
    print(line.strip())
    
# Closing the file
file.close()
