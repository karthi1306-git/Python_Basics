with open("D:\TC Analysis Report.txt","r") as File1:
    file_Content=File1.read()
    print(file_Content)
    File1.close()
    print(File1.closed)
    #print(file_Content)


with open("D:\TC Analysis Report.txt","r") as File2:
    print(File2.readline(4))
    for line in File2:
        print(line)

Lines=["This is Line1\n","This is Line2\n","This is Line3\n"]
with open("D:\TC Analysis Report.txt","w") as File3:
    for line in Lines:
        File3.write(line)


