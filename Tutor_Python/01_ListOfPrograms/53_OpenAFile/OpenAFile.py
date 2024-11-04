try:
    f=open("ram.txt",'w')
    #f=open("data.txt",'a')
    #f=open("data.txt",'r')
    #print(f.read())
    #print(f.readline())
    """
    for line in f:
        print(line)
    """
    f.write("\nThis is New Line")
except FileNotFoundError:
    print("File not Found")
else:
    print("Thank You")
    f.close()