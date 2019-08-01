#!/usr/bin/ python

'''
************************************************************************************
This module performs various mathematical calculations such as :

1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Square Root
6.  Cubic Root
7.  Factorial
8.  Power
9.  Modulus
10. Length of a Vector
11. Cosine of an angle in radians,
12. Sine of an angle in radians,
13. Tan of an angle in radians
14. Inverse cosine
15. Inverse sine
16. Inverse tan
17. Logarathmic for any given base, default base is e.
18. Store a value in memory
19. Clear the memory

************************************************************************************
'''

from __future__ import print_function
from collections import OrderedDict
import math
import os
import sys
import re
import time
import csv


Memory_store=""
DATEFORMAT = '%Y-%m-%d'
LOGPATH="./reports/"
Test_Mode=True
Operations_track = OrderedDict()
last_operation_date=time.strftime(DATEFORMAT)

def re_Check(string): 
  
    # Check for special characters exisitent in the input
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]') 
      
    # Pass the string in search method of the regex object.     
    if(regex.search(string) == None): 
        print("Input is accepted\n") 
        return 0
          
    else: 
        print("Input cannot contain any special characters i.e. [@_!#$%^&*()<>?/|}{~:]\tPlease enter again\n")
        return 1

def generate_Reports():
    global Memory_store, last_operation_date, LOGPATH
    filepath = LOGPATH + last_operation_date + ".csv"

    try:
        with open(filepath,'w') as file:
            csv_writer=csv.writer(file, delimiter='\t')
            csv_writer.writerow('Operations executed by the user on ' + last_operation_date + ':')
            for k,v in Operations_track.items():
                csv_writer.writerow(k + ':' + str(v))

    except IOError:
        print('Unable to create report for : ' + last_operation_date)




def addition(num1=0,num2=0):

    global Test_Mode
    if Test_Mode==True:
        return num1 + num2
    else:

    
        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)


        print("You have selected addition operation\n")

        while True:
            input1=str(input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break

        if input1==None and input2==None:
            input1=num1
            input2=num2
        result=float(input1) + float(input2)
        print("{0} + {1} = {2}".format(input1,input2,result))


        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['addition']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['addition']+=1

        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
                Memory_store=str(result)
        else:
                Memory_store=Memory_store


def subtraction(num1=0,num2=0):

    global Test_Mode
    if Test_Mode==True:
        return num1 - num2
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)

        print("You have selected subtraction operation\n")

        while True:
            input1=str(input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break

        result=float(input1) - float(input2)
        print("{0} - {1} = {2}".format(input1,input2,result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['subtraction']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['subtraction']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def multiplication(num1=0,num2=0):

    global Test_Mode
    if Test_Mode==True:
        return num1 * num2
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)

        print("You have selected multiplication operation\n")

        while True:
            input1=str(input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break

        result=float(input1) * float(input2)
        print("{0} * {1} = {2}".format(input1,input2,result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['multiplication']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['multiplication']+=1

        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def division(num1=0,num2=0):

    global Test_Mode
    if Test_Mode==True:
        return num1 / num2
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected division operation\n")

        while True:
            input1=str(input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(input('Enter the second number\n'))
            if((re_Check(input2)==0) and round(float(input2),2) != 0):
                break
            elif round(float(input2),2) == 0:
                print("Cannot divide by 0\n")
                continue

        result=float(input1) / float(input2)
        print("{0} / {1} = {2}".format(input1,input2,result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['division']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['division']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store


def sqrt(number=0):

    global Test_Mode
    if Test_Mode==True:
        return math.sqrt(number)
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected square root operation\n")

        while True:
            number=str(input('Enter the number\n'))
            if(re_Check(number)==0):
                break

        result=math.sqrt(abs(float(number)))
        print("sqrt({0}) : {1}".format(number, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['sqrt']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['sqrt']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def crt(number=0):

    global Test_Mode
    if Test_Mode==True:
        number=abs(float(number))
        result=round((number)**(1./3.),3)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected cube root operation\n")

        while True:
            number=str(input('Enter the number\n'))
            if(re_Check(number)==0):
                break

        number=abs(float(number))
        result=round((number)**(1./3.),3)
        print("cubic_rt({0}) : {1}".format(number, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['crt']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['crt']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def factorial(number=0):

    global Test_Mode
    if Test_Mode==True:
        number=abs(int(number))
        result=math.factorial(number)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected factorial operation\n")

        while True:
            number=str(input('Enter the number\n'))
            if(re_Check(number)==0):
                break

        number=abs(int(number))
        result=math.factorial(number)
        print("factorial({0}) : {1}".format(number, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['factorial']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['factorial']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def power(base=0,power=0):
    global Test_Mode
    if Test_Mode==True:
        result=float(base) ** float((power))
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected power operation\n")

        while True:
            base=str(input('Enter the base number\n'))
            if(re_Check(base)==0):
                break

        while True:
            power=str(input('Enter the power value\n'))
            if(re_Check(power)==0):
                break

        result=float(base) ** float((power))
        print("{0} ** {1} = {2}".format(base,power,result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['power']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['power']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def modulus(num1=0,num2=0):
    global Test_Mode
    if Test_Mode==True:
        result=abs(int(num1)) % abs(int(num2))
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected modulus operation\n")

        while True:
            input1=str(input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break
        
        result=abs(int(input1)) % abs(int(input2))

        print("({0}) % {1} : {2}".format(input1, input2, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['modulus']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['modulus']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store


def vector_Length(num1=0,num2=0):

    global Test_Mode
    if Test_Mode==True:
        result=round(math.sqrt((abs(int(num1)) ** 2) + (abs(int(num2) ** 2))),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected vector length operation\n")

        while True:
            input1=str(input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break
        
        result=round(math.sqrt((abs(int(input1)) ** 2) + (abs(int(input2) ** 2))),2)

        print("Vector Length ({0},{1}) : {2}".format(input1, input2, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['vector']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['vector']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def cos(format='degrees',angle=0):

    global Test_Mode
    if Test_Mode==True:
        if format=="degrees":
            angle=float((math.pi/180)*(float(angle)))
            result=round(math.cos(float(angle)),2)
        elif format=="radians":
            result=round(math.cos(float(angle)),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected cosine operation\n")

        while True:
            angle_format=str(input("Angle in degrees or radians ?\n"))
            if angle_format == "radians":
                while True:
                    angle=str(input('Enter the angle in radians\n'))
                    if(re_Check(angle)==0):
                        break
                break
                        
            elif angle_format == "degrees":
                while True:
                    angle=str(input('Enter the angle in degrees\n'))
                    if(re_Check(angle)==0):
                        angle=float((math.pi/180)*(float(angle)))
                        break
                break

        result=math.cos(float(angle))
        print("cos({0}) : {1}".format(angle, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['cos']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['cos']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def sin(format='degrees',angle=0):

    global Test_Mode
    if Test_Mode==True:
        if format=="degrees":
            angle=float((math.pi/180)*(float(angle)))
            result=round(math.sin(float(angle)),2)
        elif format=="radians":
            result=round(math.sin(float(angle)),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected sine operation\n")

        while True:
            angle_format=str(input("Angle in degrees or radians ?\n"))
            if angle_format == "radians":
                while True:
                    angle=str(input('Enter the angle in radians\n'))
                    if(re_Check(angle)==0):
                        break
                break
                        
            elif angle_format == "degrees":
                while True:
                    angle=str(input('Enter the angle in degrees\n'))
                    if(re_Check(angle)==0):
                        angle=float((math.pi/180)*(float(angle)))
                        break
                break

        result=math.sin(float(angle))
        print("sin({0}) : {1}".format(angle, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['sin']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['sin']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def tan(format='degrees',angle=0):

    global Test_Mode
    if Test_Mode==True:
        if format=="degrees":
            angle=float((math.pi/180)*(float(angle)))
            result=round(math.tan(float(angle)),2)
        elif format=="radians":
            result=round(math.tan(float(angle)),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected tan operation\n")

        while True:
            angle_format=str(input("Angle in degrees or radians ?\n"))
            if angle_format == "radians":
                while True:
                    angle=str(input('Enter the angle in radians\n'))
                    if(re_Check(angle)==0):
                        break
                break
                        
            elif angle_format == "degrees":
                while True:
                    angle=str(input('Enter the angle in degrees\n'))
                    if(re_Check(angle)==0):
                        angle=float((math.pi/180)*(float(angle)))
                        break
                break

        result=math.tan(float(angle))
        print("tan({0}) : {1}".format(angle, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['tan']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['tan']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store


def acos(number):

    global Test_Mode
    if Test_Mode==True:
        number=float(number)
        result=round(math.acos(number),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected the inverse cosine operation\n")

        while True:
            value=str(input('Enter the number to compute its Acos\n'))
            if(re_Check(value)==0):
                break

        value=float(value)
        result=math.acos(value)
        print("Acos({0}) : {1}".format(value, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['acos']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['acos']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store

def asin(number):
    global Test_Mode
    if Test_Mode==True:
        number=float(number)
        result=round(math.asin(number),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected the inverse sine operation\n")

        while True:
            value=str(input('Enter the number to compute its Asin\n'))
            if(re_Check(value)==0):
                break

        value=float(value)
        result=math.asin(value)
        print("Asin({0}) : {1}".format(value, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['asin']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['asin']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def atan(number):
    global Test_Mode
    if Test_Mode==True:
        number=float(number)
        result=round(math.atan(number),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected the inverse tan operation\n")

        while True:
            value=str(input('Enter the number to compute its Atan\n'))
            if(re_Check(value)==0):
                break

        value=float(value)
        result=math.atan(value)
        print("Atan({0}) : {1}".format(value, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['atan']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['atan']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store


def var_Remove():

    global Test_Mode
    if Test_Mode:
        return None
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected to clear the memory\n")
        Memory_store=None

        print("No values are being stored.\n")
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['var_Remove']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['var_Remove']+=1


def var_Store(number):
    global Test_Mode, Memory_store
    if Test_Mode:
        Memory_store=number
        return Memory_store
    else:

        global last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected to store a data in memory\n")
        while True:
            data=str(input('Enter the number\n'))
            if(re_Check(data)==0):
                break

        Memory_store=data
        print("Given value : {0}, stored in memory\n".format(Memory_store))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['var_Store']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['var_Store']+=1

def print_Store():
    global Memory_store, last_operation_date
    operation_date=time.strftime(DATEFORMAT)
    print("The stored value is {0}".format(Memory_store))
    if (operation_date != last_operation_date):
        generate_Reports()
        for k,v in Operations_track.items():
            Operations_track[k]=0
        Operations_track['print_Store']+=1
        last_operation_date = operation_date
    elif operation_date == last_operation_date:
        Operations_track['print_Store']+=1


def log(num1=0,num2=0):

    global Test_Mode
    if Test_Mode==True:
        result=round(math.log(float(num1),int(num2)),2)
        return result
    else:

        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected logarathmic operation\n")

        while True:
            number=str(input('Enter the number whose log is required\n'))
            if(re_Check(number)==0):
                break

        while True:
            base=str(input('Enter the base, default base : e\n'))
            if base == "":
                print("Computing natural log\n")
                break

            if(re_Check(base)==0):
                break
        
        result=math.log(float(number),int(base))

        print("log({0} base {1}) : {2}".format(number, base, result))
        if (operation_date != last_operation_date):
            generate_Reports()
            for k,v in Operations_track.items():
                Operations_track[k]=0
            Operations_track['log']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            Operations_track['log']+=1
        store_result=str(input("Do you want to store this result, yes or no ?\n"))
        if store_result == "yes":
            Memory_store=str(result)
        else:
            Memory_store=Memory_store



def add_subtract_Store(operation="add",num1=0,num2=0):
    global Test_Mode
    if Test_Mode==True:
        if operation=="add":
            result =num1 + num2
            
        elif operation=="sub":
            result=num1 - num2
        return result
    else:
        
        global Memory_store, last_operation_date
        operation_date=time.strftime(DATEFORMAT)
        print("You have selected add/sub operation on MR value.\n")

        while True:
            oper=str(input('Please select the desired operation, add or sub ?\n'))
            if(re_Check(oper)==0):
                break

        while True:
            operand=str(input('Enter the number used for this operation.\n'))
            if(re_Check(operand)==0):
                break

        if oper == "add":
            result = float(Memory_store) + float(operand)
            print("{0} + {1} = {2}\n".format(Memory_store, operand, result))
            if (operation_date != last_operation_date):
                generate_Reports()
                for k,v in Operations_track.items():
                    Operations_track[k]=0
                Operations_track['add_subtract_Store']+=1
                last_operation_date = operation_date
            elif operation_date == last_operation_date:
                Operations_track['add_subtract_Store']+=1
            store_result=str(input("Do you want to store this result, yes or no ?\n"))
                
            if store_result == "yes":
                Memory_store=str(result)
            else:
                Memory_store=Memory_store
                
        elif oper =="sub":
            result = float(Memory_store) - float(operand)
            print("{0} - {1} = {2}\n".format(Memory_store, operand, result))
            if (operation_date != last_operation_date):
                generate_Reports()
                for k,v in Operations_track.items():
                    Operations_track[k]=0
                Operations_track['add_subtract_Store']+=1
                last_operation_date = operation_date
            elif operation_date == last_operation_date:
                Operations_track['add_subtract_Store']+=1
            store_result=str(input("Do you want to store this result, yes or no ?\n"))
                
            if store_result == "yes":
                Memory_store=str(result)
            else:
                Memory_store=Memory_store




def calculator_Operation(argument):
    global Test_Mode
    # Get the function from Operation_Dict dictionary
    func = Operation_Dict.get(argument, "Enter a valid number\n")
    # Execute the function
    Test_Mode=False
    return func()


'''
Implementing switch case on the user input.
'''
Operation_Dict={1:addition,
2:subtraction,
3:multiplication,
4:division,
5:sqrt,
6:crt,
7:factorial,
8:power,
9:modulus,
10:vector_Length,
11:cos,
12:sin,
13:tan,
14:acos,
15:asin,
16:atan,
17:log,
18: var_Store,
19: print_Store,
20: var_Remove,
21: add_subtract_Store}



'''
Dictionary to keep a track of no.of operations requested per day for each type.
'''
Operations_track={'addition':0,
'subtraction':0,
'multiplication':0,
'division':0,
'sqrt':0,
'crt':0,
'factorial':0,
'power':0,
'modulus':0,
'vector':0,
'cos':0,
'sin':0,
'tan':0,
'acos':0,
'asin':0,
'atan':0,
'log':0,
'var_Store':0,
'print_Store':0,
'var_Remove':0,
'add_subtract_Store':0}


'''
This function prompts the user for an input.
Required arguments includes :

1. Operands
2. Operator
'''
def main():

    print("Refer to the below menu for desired operation:\n+++++++++++++++++++++++++++++++++++++++++\n"\
        "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Cubic Root\n"\
            "7. Factorial\n8. Power\n9. Modulus\n10. Length of a Vector\n11. Cosine of an angle (radians/degrees)\n"
                "12. Sine of an angle (radians/degrees)\n13. Tan of an angle (radians/degrees)\n"
                    "14. Inverse cosine\n15. Inverse sine\n16. Inverse tan\n17. Logarathmic\n"
                        "18. Store a value in memory register.\n19. Display the value stored in memory register.\n"
                        "20. Remove the value stored in memory register.\n21. Use stored value for calculations\n"
                "+++++++++++++++++++++++++++++++++++++++++\n\n")

    global Operation_Dict
    while True:
        user_input=int(input('Press the asscoiated number for the desired operation\n'))
        if user_input>21:
            print("Please enter number within the range 1-21.\n")
            continue
        calculator_Operation(user_input)


if __name__=="__main__":
    print("Welcome to a simple yet powerful calculator by Megasoft.\n")
    main()