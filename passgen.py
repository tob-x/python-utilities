"""
    74 6F 62

    author:tob
    desc: simple passgen

"""

import random
import getopt
import sys
import string

def usage():
    print(f"Usage: {sys.argv[0].split('/')[-1]} [-h] [-d | --difficulty=<difficulty level>] [-l | --length=<length>] [-c | --count=<iterations>]")

def generate_string(length,charlist):
    str = ""
    for i in range(length):
        k = random.randrange(len(charlist))
        str += f"{charlist[k]}"
    print(str)
    

def main(argv):
    length = 12
    dif = 2
    iterations = 1
    try:
        opts, args = getopt.getopt(argv, "hdl:c:", ["help", "difficulty","length=","count="])
    except getopt.GetoptError:
        usage()
        sys.exit(-1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit(0)
        elif opt in ("-d","--difficulty"):
            dif = int(arg)
        elif opt in ("-l","--length"):
            length = int(arg)
        elif opt in ("-c", "--count"):
            iterations = int(arg)
    
    if dif == -1 :
        charlist = string.digits
    elif dif == 0 :
        charlist = string.hexdigits
    elif dif == 1:
        charlist = string.ascii_letters + string.digits
    elif dif == 2:
        charlist = string.digits + string.ascii_letters + "?!$%&()[]{}:_-"
    
    while iterations:
        generate_string(length, charlist)
        iterations -= 1

    
if __name__ == "__main__":
    main(sys.argv[1:])