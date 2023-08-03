# opening and creating new .txt file
with open("Rahul Shetty API Course\\File Handling Important Questions\\abc.txt", 'r') as r, open('Rahul Shetty API Course\\File Handling Important Questions\\output.txt', 'w') as o:
    for line in r:
       o.write(line)

f = open("Rahul Shetty API Course\\File Handling Important Questions\\output.txt", "r")
result = [line.strip() for line in f.readlines()]
print(result)
# print("New text file:\n",f.read())
