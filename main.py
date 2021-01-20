# ScriptName: main.py
# Author: Jason Quinlan

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
#from functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print(a_function())
    print(what_am_I([1, "It's", 1.2, "fun", {"hi": "you"}, "time", 2],"all"))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
