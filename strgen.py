"""
    74 6F 62

    author:tob
    desc: simple string gen with options

"""
import random
import getopt
import sys

def usage():
    print(f"Usage: {sys.argv[0].split('/')[-1]} [-h] [-x] [-l | --length=<length>] [-c | --count=<iterations>]")

def generate_string(length,charlist):
    str = ""
    for i in range(length):
        k = random.randrange(len(charlist))
        str += f"{charlist[k]}"
    # for i in range(length):
    #     for i in range(random.randrange(0,len(charlist))):
    #         str = "".join(charlist[i])
    print(str)
    

def main(argv):
    hexa = False
    length = 16
    hex_chars = "0123456789abcdef"
    ascii_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    iterations = 1
    try:
        opts, args = getopt.getopt(argv, "hxl:c:", ["help", "hexa","length=","count="])
    except getopt.GetoptError:
        usage()
        sys.exit(-1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit(0)
        elif opt in ("-x","--hexa"):
            hexa = True
        elif opt in ("-l","--length"):
            length = int(arg)
        elif opt in ("-c", "--count"):
            iterations = int(arg)

    if hexa:
        while iterations:
            generate_string(length, hex_chars)
            iterations -= 1
    else:
        while iterations:
            generate_string(length, ascii_chars)
            iterations -= 1

    
if __name__ == "__main__":
    main(sys.argv[1:])