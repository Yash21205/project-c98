from cgitb import text


def swapping_file():
    file1="text1.txt"
    file2="text2.txt"
    
    with open(file1,"r") as f1 :
        data1=f1.read()
      
    with open(file2,"r") as f2 :
        data2=f2.read()
          
    with open(file1,"w") as f1 :
        f1.write(data2)
      
    with open(file2,"w") as f2 :
        f2.write(data1)
swapping_file()