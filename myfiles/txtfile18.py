#manu driven text file application using match case]
import os
import shutil
from unittest import case
filename="c:/pythoncode/myfiles/mydata,=.txt"
while True:
    print("\n" + "=" * 50)
    print("Text file management system")
    print("=" *50)
    print("1. create a new file")
    print("2. Append data")
    print("3. copy file")
    print("4. Display file")
    print("5. Rename file")
    print("6. edit file")
    print("7. delete file")
    print("8. count lines,words, characters")
    print("9. exit")
    print("=" * 50)
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            f=open(filename,"w")
            print("\n enter text(Type end to stop)")
            while True:
                line=input()
                if line.upper()=="END":
                    break
                f.write(line+"/n")
                f.close()
                print("file created successfully")
#--------------------------------------------------------------
        case 2:
            if os.path.exists(filename):
                f = open(filename, "a")
                print("\nEnter text to append (Type END to stop)")
                while True:
                    line = input()
                    if line.upper() == "END":
                        break
                    f.write(line + "\n")
                f.close()
                print("Data Appended Successfully.")
            else:
                print("File does not exist.")
# --------------------------------------------------
        case 3:
            if os.path.exists(filename):
                newfile = input("Enter copy file name : ")
                shutil.copy(filename, "c:/mypythoncode/myfiles/" + newfile)
                print("File Copied Successfully.")
            else:
                print("File does not exist.")
# --------------------------------------------------
        case 4:
            if os.path.exists(filename):
                f = open(filename, "r")
                print("\n------ FILE CONTENT ------\n")
                print(f.read())
                f.close()
            else:
                print("File does not exist.")
# --------------------------------------------------
        case 5:
            if os.path.exists(filename):
                newname = input("Enter new file name : ")
                newpath = "c:/mypythoncode/myfiles/" + newname
                os.rename(filename, newpath)
                filename = newpath
                print("File Renamed Successfully.")
            else:
                print("File does not exist.")
# --------------------------------------------------
        case 6:
            if os.path.exists(filename):
                f = open(filename, "w")
                print("\nEnter new content (Type END to stop)")
                while True:
                    line = input()
                    if line.upper() == "END":
                        break
                    f.write(line + "\n")
                f.close()
                print("File Updated Successfully.") 
            else:
                print("File does not exist.")
# --------------------------------------------------
        case 7:
            if os.path.exists(filename):
                os.remove(filename)
                print("File Deleted Successfully.")
            else:
                print("File does not exist.")
# --------------------------------------------------
        case 8:
            if os.path.exists(filename):
                f = open(filename, "r")
                data = f.read()
                f.close()

                lines = len(data.splitlines())
                words = len(data.split())
                characters = len(data)

                print("\n------ FILE STATISTICS ------")
                print("Total Lines      :", lines)
                print("Total Words      :", words)
                print("Total Characters :", characters)
            else:
                print("File does not exist.")
 # --------------------------------------------------
        case 9:
            print("\nThank You...")
            print("Exiting Program...")
            break
 # --------------------------------------------------
        case _:
            print("Invalid Choice.")






