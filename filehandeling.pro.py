import os
print("-----FILE HANDELING IN PYTHON-----")
print("1.create the file\n2.read the file\n3.list the files\n4.edit the files\n5.delete the files\n6.end program\n")
while True:
    a=int(input("enter your choice:"))
    def f():  
        print("1.create the file")
        print("2.read the file")
        print("3.list the files")
        print("4.edit the files")
        print("5.delete the files")
        print("6.end program")
    match a:
        case 1:
            print("\n1.creating the file..")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"w")
            file.write("hello ")
            print("file created successfully")
            print("--------------------------------")
            f()
            
        
        case 2:
            print("2.reading the file..")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"r")
            print(file.read())
            print("-------------")
            f()
            
        case 3:
            print("3.listing the files..")
            print("listed files are:")
            print("--------------------------------")
            path="D:\supriya.bca"
            files=os.listdir(path)
            for file in files:
                print(file)
            f()
            
        case 4:
            print("4.editing the file...")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"a")
            (file.write("and edited "))
            print("--------------------------------")
            f()
            
        case 5:
            print("5.deleting the file..")
            name=input("enter the file name:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"\ndeleted successfully")
            print("--------------------------------")
            f()
            
        case 6:
            print("6.end program")
            print("-----you have suceessfully completed your program-----")
        case _:
            print("oops..sinvalid number!!!")
            break
