#import libraries
import math


#Declaring Variables
input_text = 0 #User reply to input prompt
remaining_digits  = 0 #Remaining digits after calculation

#Num_to_Formula Variables
num1 = 0 #First number in the formula
num2 = 0 #Second number in the formula


#Decaring Functions
def Num_to_Formula(remaining_digits): # Convert Number to a formula
    
    #calculate the formula
    global num1, num2
    num1 = math.sqrt(remaining_digits) #




    print(num1 + "^" + num2, end='') #print part of the formula
    if remaining_digits >= 10**20:
        Num_to_Formula(remaining_digits) #Recursively call the function with reduced remaining digits
    print(remaining_digits) #print remaining digits if any
    input("Press Enter to exit...")






#other random stuff/brainstorming

input("1)Encode 2)Decode 3)Settings: ")

if input_text == 1: #If user chooses to encode
    input_text = input("Encode: ")
    print(bin(input_text)[2:]) #Print the binary representation
    Num_to_Formula(int(input_text, 2)) #Convert to binary then send to Num_to_Formula function
else:
    print("jeh34a")