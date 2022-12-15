# Title: Calculate Sum Program
# Program created by William Schaeffer
# CPS 313
# P. 358, Exercise 5, Calculate Sum Program
# 02.01.22

# This program will calculate the sum of numbers stored in numbers.txt
# This example will work even if the numbers.txt has numbers added to it or taken away

# Main Function

def main():
    
    welcome_function()                                  # Call welcome function
    
    number_file = open('numbers.txt', 'r')              # Open numbers.txt
    
    value = 0                                           # set value and line to 0
    line = 0

    fileInput = number_file.readline()                  # read line and store in fileInput

    while fileInput != '':                              # while fileInput is not an empty string
        value += int(fileInput)                         # increment value after converting fileInput from string to int

        fileInput = number_file.readline()              # read line and store in fileInput

        line += 1                                       # increment line for each inputed line

    avgValue = value / line                             # Calculate average value by dividing total value by number of inputs

    print(f'{value} is the total of the values in numbers.txt')
    print(f'{avgValue} is the average of the values in numbers.txt')

    number_file.close()                                 # close numbers.txt


# Function Definition

def welcome_function():                                 # Function to welcome user

    print(f'Welcome to the Calculate Sum Program!')
    

main()                                                  # Call main function

