#user defined exception
import os
import subprocess
subprocess.run("cls",shell=True)
class InvalidAgeError(Exception):
    pass
try:
    age=int(input("Enter your age...:"))
    if(age<=18):
        raise InvalidAgeError
    else:
        print("you are eligible to vote")
except InvalidAgeError:
    print("you are not eligible to vote")
finally:
    print("ask to others to vote")
