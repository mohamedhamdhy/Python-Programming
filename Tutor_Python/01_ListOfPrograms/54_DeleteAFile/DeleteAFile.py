import os
 
if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("File Not Found")