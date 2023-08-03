with open('Rahul Shetty API Course\\File Handling Important Questions\\abc.txt') as reader, open('Rahul Shetty API Course\\File Handling Important Questions\\output.txt', 'w') as writer:
    content = reader.readlines()
    
    for line in reversed(content):
        writer.write(line)
    
    ## without using built-in functions 
    # for line in content[::-1]:
    #     writer.write(line)
        