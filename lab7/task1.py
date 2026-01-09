# # functions
""" Update the function printTwice so that it prints the input argument two times but on the
same line separated by a white space. Then in main program, take a string input from user and
use this function to print it twice on the screen.
"""
message = input("Enter any message: ")
def printTwice():
    print(message, message)
printTwice()