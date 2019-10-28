lines = ["this is the first line.","this is second line.","this is the third line."]
with open ("test.txt","w") as fp:
    for line in lines:
        fp.write(line+"\n")
        
with open("test.txt", "r") as fp:
    content= fp.read()
    print(content)

