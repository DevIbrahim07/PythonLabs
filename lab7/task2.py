
""" A function can have more than one input arguments. Create a function with two input arguments
as printTimes(s,n) where s and n are those input arguments. s should be treated as string
to be printed on screen and n is the number of times that string be printed. Take input the string
and number of times user wants to print and display the output. Essentially, it is similar to first
task but instead of printing twice now the string will be printed as many times as required."""


def printTimes(s, n):
    result = s * n 
    print(result)

message = input("Enter any message: ")
times = int(input( "times to repeat: "))
printTimes(message, times)





