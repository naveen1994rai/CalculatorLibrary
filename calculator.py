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
20. Remove the value stored in memory register.
21. Use stored value for calculations
22. Generate reports for given day.
23. Generate reports within the given dates.

************************************************************************************
'''

from __future__ import print_function
from collections import OrderedDict
import math
import sqlite3 as lite
import os
import sys
import re
import time
import csv
import json
from datetime import datetime


memory_store=""
dateformat = '%Y-%m-%d'
logpath="./reports/"
test_mode=True
operations_track = OrderedDict()
last_operation_date=datetime.now().strftime(dateformat)
operations_count=1
con=None
new_conn=True


try:
    con = lite.connect('calc.db')
    cur = con.cursor()  
    
    cur.execute("CREATE TABLE IF NOT EXISTS Calculations(Id INT, Operation TEXT, Count INT, Variables TEXT, answer REAL, MR REAL, Executed TEXT)")

except lite.Error as e:   
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:    
    if con:
        con.close()



def re_Check(string): 
  
    # Check for special characters exisitent in the input
    regex = re.compile('[`@_!#$%^&*()<>?/|}{~:]') 
      
    # Pass the string in search method of the regex object.     
    if(regex.search(string) == None): 
        print("Input is accepted\n") 
        return 0
          
    else: 
        print("Input cannot contain any special characters i.e. [@_!#$%^&*()<>?/|}{~:]\tPlease enter again\n")
        return 1


def addition(num1=0,num2=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        return num1 + num2
    else:
        
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected addition operation\n")
        while True:
            input1=str(raw_input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break
        while True:
            input2=str(raw_input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break
        if input1==None and input2==None:
            input1=num1
            input2=num2
        answer=float(input1) + float(input2)
        print("{0} + {1} = {2}".format(input1,input2,answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['addition']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['addition']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(input1) + "," + str(input2)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Add',))
                        result=cur.fetchall()
                        operations_track['addition']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Add', operations_track['addition'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1


def subtraction(num1=0,num2=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        return num1 - num2
    else:
        operation_date=datetime.now().strftime(dateformat)

        print("You have selected subtraction operation\n")

        while True:
            input1=str(raw_input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(raw_input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break

        answer=float(input1) - float(input2)
        print("{0} - {1} = {2}".format(input1,input2,answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['subtraction']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['subtraction']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(input1) + "," + str(input2)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Sub',))
                        result=cur.fetchall()
                        operations_track['subtraction']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Sub', operations_track['subtraction'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def multiplication(num1=0,num2=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        return num1 * num2
    else:
        operation_date=datetime.now().strftime(dateformat)

        print("You have selected multiplication operation\n")

        while True:
            input1=str(raw_input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(raw_input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break

        answer=round(float(input1) * float(input2),2)
        print("{0} * {1} = {2}".format(input1,input2,answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['multiplication']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['multiplication']+=1

        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(input1) + "," + str(input2)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Mul',))
                        result=cur.fetchall()
                        operations_track['multiplication']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Mul', operations_track['multiplication'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def division(num1=0,num2=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        return num1 / num2
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected division operation\n")

        while True:
            input1=str(raw_input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(raw_input('Enter the second number\n'))
            if((re_Check(input2)==0) and round(float(input2),2) != 0):
                break
            elif round(float(input2),2) == 0:
                print("Cannot divide by 0\n")
                continue

        answer=round(float(input1) / float(input2),2)
        print("{0} / {1} = {2}".format(input1,input2,answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['division']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['division']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(input1) + "," + str(input2)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Div',))
                        result=cur.fetchall()
                        operations_track['division']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Div', operations_track['division'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1


def sqrt(number=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        return math.sqrt(number)
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected square root operation\n")

        while True:
            number=str(raw_input('Enter the number\n'))
            if(re_Check(number)==0):
                break

        answer=round(math.sqrt(abs(float(number))),2)
        print("sqrt({0}) : {1}".format(number, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['sqrt']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['sqrt']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(number)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Sqrt',))
                        result=cur.fetchall()
                        operations_track['sqrt']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Sqrt', operations_track['sqrt'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def crt(number=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        number=abs(float(number))
        answer=round((number)**(1./3.),3)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected cube root operation\n")

        while True:
            number=str(raw_input('Enter the number\n'))
            if(re_Check(number)==0):
                break

        number=abs(float(number))
        answer=round((number)**(1./3.),2)
        print("cubic_rt({0}) : {1}".format(number, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['crt']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['crt']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(number)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Crt',))
                        result=cur.fetchall()
                        operations_track['crt']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Crt', operations_track['crt'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def factorial(number=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        number=abs(int(number))
        answer=math.factorial(number)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected factorial operation\n")

        while True:
            number=str(raw_input('Enter the number\n'))
            if(re_Check(number)==0):
                break

        number=abs(int(number))
        answer=math.factorial(number)
        print("factorial({0}) : {1}".format(number, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['factorial']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['factorial']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(number)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Factorial',))
                        result=cur.fetchall()
                        operations_track['factorial']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Factorial', operations_track['factorial'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def power(base=0,power=0):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        answer=float(base) ** float((power))
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected power operation\n")

        while True:
            base=str(raw_input('Enter the base number\n'))
            if(re_Check(base)==0):
                break

        while True:
            power=str(raw_input('Enter the power value\n'))
            if(re_Check(power)==0):
                break

        answer=round(float(base) ** float((power)),2)
        print("{0} ** {1} = {2}".format(base,power,answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['power']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['power']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used={'number':base,'power':power}
            var_json=str(var_used)
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Power',))
                        result=cur.fetchall()
                        operations_track['power']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Power', operations_track['power'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def modulus(num1=0,num2=0):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        answer=abs(int(num1)) % abs(int(num2))
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected modulus operation\n")

        while True:
            input1=str(raw_input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(raw_input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break
        
        answer=abs(int(input1)) % abs(int(input2))

        print("({0}) % {1} : {2}".format(input1, input2, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['modulus']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['modulus']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(input1) + ',' + str(input2)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Modulus',))
                        result=cur.fetchall()
                        operations_track['modulus']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Modulus', operations_track['modulus'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1


def vector_Length(num1=0,num2=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        answer=round(math.sqrt((abs(int(num1)) ** 2) + (abs(int(num2) ** 2))),2)
        return answer
    else: 
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected vector length operation\n")

        while True:
            input1=str(raw_input('Enter the first number\n'))
            if(re_Check(input1)==0):
                break

        while True:
            input2=str(raw_input('Enter the second number\n'))
            if(re_Check(input2)==0):
                break
        
        answer=round(math.sqrt((abs(int(input1)) ** 2) + (abs(int(input2) ** 2))),2)

        print("Vector Length ({0},{1}) : {2}".format(input1, input2, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['vector']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['vector']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(input1) + ',' + str(input2)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Vector',))
                        result=cur.fetchall()
                        operations_track['vector']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Vector', operations_track['vector'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def cos(format='degrees',angle=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        if format=="degrees":
            angle=float((math.pi/180)*(float(angle)))
            answer=round(math.cos(float(angle)),2)
        elif format=="radians":
            answer=round(math.cos(float(angle)),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected cosine operation\n")

        while True:
            angle_format=str(raw_input("Angle in degrees or radians ?\n"))
            if angle_format == "radians":
                while True:
                    angle=str(raw_input('Enter the angle in radians\n'))
                    if(re_Check(angle)==0):
                        break
                break
                        
            elif angle_format == "degrees":
                while True:
                    angle=str(raw_input('Enter the angle in degrees\n'))
                    if(re_Check(angle)==0):
                        angle=float((math.pi/180)*(float(angle)))
                        break
                break

        answer=round(math.cos(float(angle)),2)
        print("cos({0}) : {1}".format(angle, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['cos']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['cos']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used={'angle':angle,'format':angle_format}
            var_json=str(var_used)
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Cos',))
                        result=cur.fetchall()
                        operations_track['cos']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Cos', operations_track['cos'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def sin(format='degrees',angle=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        if format=="degrees":
            angle=float((math.pi/180)*(float(angle)))
            answer=round(math.sin(float(angle)),2)
        elif format=="radians":
            answer=round(math.sin(float(angle)),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected sine operation\n")

        while True:
            angle_format=str(raw_input("Angle in degrees or radians ?\n"))
            if angle_format == "radians":
                while True:
                    angle=str(raw_input('Enter the angle in radians\n'))
                    if(re_Check(angle)==0):
                        break
                break
                        
            elif angle_format == "degrees":
                while True:
                    angle=str(raw_input('Enter the angle in degrees\n'))
                    if(re_Check(angle)==0):
                        angle=float((math.pi/180)*(float(angle)))
                        break
                break

        answer=round(math.sin(float(angle)),2)
        print("sin({0}) : {1}".format(angle, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['sin']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['sin']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used={'angle':angle,'format':angle_format}
            var_json=str(var_used)
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Sin',))
                        result=cur.fetchall()
                        operations_track['sin']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Sin', operations_track['sin'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def tan(format='degrees',angle=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        if format=="degrees":
            angle=float((math.pi/180)*(float(angle)))
            answer=round(math.tan(float(angle)),2)
        elif format=="radians":
            answer=round(math.tan(float(angle)),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected tan operation\n")

        while True:
            angle_format=str(raw_input("Angle in degrees or radians ?\n"))
            if angle_format == "radians":
                while True:
                    angle=str(raw_input('Enter the angle in radians\n'))
                    if(re_Check(angle)==0):
                        break
                break
                        
            elif angle_format == "degrees":
                while True:
                    angle=str(raw_input('Enter the angle in degrees\n'))
                    if(re_Check(angle)==0):
                        angle=float((math.pi/180)*(float(angle)))
                        break
                break

        answer=round(math.tan(float(angle)),2)
        print("tan({0}) : {1}".format(angle, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['tan']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['tan']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used={'angle':angle,'format':angle_format}
            var_json=str(var_used)
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Tan',))
                        result=cur.fetchall()
                        operations_track['tan']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Tan', operations_track['tan'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1


def acos(number=1):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        number=float(number)
        answer=round(math.acos(number),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected the inverse cosine operation\n")

        while True:
            value=str(raw_input('Enter the number to compute its Acos\n'))
            if(re_Check(value)==0):
                break

        value=float(value)
        answer=round(math.acos(value),2)
        print("Acos({0}) : {1}".format(value, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['acos']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['acos']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(value)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Acos',))
                        result=cur.fetchall()
                        operations_track['acos']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Acos', operations_track['acos'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1

def asin(number=1):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        number=float(number)
        answer=round(math.asin(number),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected the inverse sine operation\n")

        while True:
            value=str(raw_input('Enter the number to compute its Asin\n'))
            if(re_Check(value)==0):
                break

        value=float(value)
        answer=round(math.asin(value),2)
        print("Asin({0}) : {1}".format(value, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['asin']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['asin']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(value)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Asin',))
                        result=cur.fetchall()
                        operations_track['asin']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Asin', operations_track['asin'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def atan(number=1):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        number=float(number)
        answer=round(math.atan(number),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected the inverse tan operation\n")

        while True:
            value=str(raw_input('Enter the number to compute its Atan\n'))
            if(re_Check(value)==0):
                break

        value=float(value)
        answer=round(math.atan(value),2)
        print("Atan({0}) : {1}".format(value, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['atan']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['atan']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=str(value)
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Atan',))
                        result=cur.fetchall()
                        operations_track['atan']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Atan', operations_track['atan'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def log(num1=0,num2=0):

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        answer=round(math.log(float(num1),int(num2)),2)
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected logarathmic operation\n")

        while True:
            number=str(raw_input('Enter the number whose log is required\n'))
            if(re_Check(number)==0):
                break

        while True:
            base=str(raw_input('Enter the base, default base : e\n'))
            if base == "":
                print("Computing natural log\n")
                break

            if(re_Check(base)==0):
                break
        
        answer=round(math.log(float(number),int(base)),2)

        print("log({0} base {1}) : {2}".format(number, base, answer))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['log']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['log']+=1
        store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
        if store_answer == "yes":
            memory_store=float(answer)
        else:
            memory_store=memory_store
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used={'number':number,'base':base}
            var_json=str(var_used)
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Log',))
                        result=cur.fetchall()
                        operations_track['log']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Log', operations_track['log'], var_json, answer, memory_store, time))
            con.commit()
            operations_count+=1



def var_Remove():

    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode:
        return None
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected to clear the memory\n")
        memory_store=None

        print("No values are being stored.\n")
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['var_Remove']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['var_Remove']+=1
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=None
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Clear Memory',))
                        result=cur.fetchall()
                        operations_track['var_Remove']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Clear Memory', operations_track['var_Remove'], var_json, memory_store, memory_store, time))
            con.commit()
            operations_count+=1


def var_Store(number=0):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn, memory_store
    if test_mode:
        memory_store=number
        return memory_store
    else:
        global last_operation_date
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected to store a data in memory\n")
        while True:
            data=str(raw_input('Enter the number\n'))
            if(re_Check(data)==0):
                break

        memory_store=data
        print("Given value : {0}, stored in memory\n".format(memory_store))
        if (operation_date != last_operation_date):
            
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['var_Store']+=1
            last_operation_date = operation_date
        elif operation_date == last_operation_date:
            operations_track['var_Store']+=1
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=None
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Store Memory',))
                        result=cur.fetchall()
                        operations_track['var_Store']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Store Memory', operations_track['var_Store'], var_json, memory_store, memory_store, time))
            con.commit()
            operations_count+=1

def print_Store():

    global test_mode,operations_count, memory_store, last_operation_date, new_conn, memory_store
    operation_date=datetime.now().strftime(dateformat)
    print("The stored value is {0}".format(memory_store))
    if (operation_date != last_operation_date):
        
        for k,v in operations_track.items():
            operations_track[k]=0
        operations_track['print_Store']+=1
        last_operation_date = operation_date
    elif operation_date == last_operation_date:
        operations_track['print_Store']+=1
    with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=None
            var_json=var_used
            if new_conn:
                try:
                    cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                    result = cur.fetchone()
                    if (result[-1] == operation_date):
                        operations_count=result[0] + 1
                        cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Display MR',))
                        result=cur.fetchall()
                        operations_track['print_Store']=result[-1][2] + 1
                    new_conn=False
                except:
                    print("Unable to query the database\n")
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Display MR', operations_track['print_Store'], var_json, memory_store, memory_store, time))
            con.commit()
            operations_count+=1




def add_subtract_Store(operation="add",num1=0,num2=0):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    if test_mode==True:
        if operation=="add":
            answer =num1 + num2
            
        elif operation=="sub":
            answer=num1 - num2
        return answer
    else:
        operation_date=datetime.now().strftime(dateformat)
        print("You have selected add/sub operation on MR value.\n")

        while True:
            operation=str(raw_input('Please select the desired operation, add or sub ?\n'))
            if(re_Check(operation)==0):
                break

        while True:
            value=str(raw_input('Enter the number used for this operation.\n'))
            if(re_Check(value)==0):
                break

        if operation == "add":
            answer = float(memory_store) + float(value)
            print("{0} + {1} = {2}\n".format(memory_store, value, answer))
            if (operation_date != last_operation_date):
                
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['add_subtract_Store']+=1
                last_operation_date = operation_date
            elif operation_date == last_operation_date:
                operations_track['add_subtract_Store']+=1
            store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
                
            if store_answer == "yes":
                memory_store=float(answer)
            else:
                memory_store=memory_store
                
        elif operation =="sub":
            answer = float(memory_store) - float(value)
            print("{0} - {1} = {2}\n".format(memory_store, value, answer))
            if (operation_date != last_operation_date):
                
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['add_subtract_Store']+=1
                last_operation_date = operation_date
            elif operation_date == last_operation_date:
                operations_track['add_subtract_Store']+=1
            store_answer=str(raw_input("Do you want to store this answer, yes or no ?\n"))
                
            if store_answer == "yes":
                memory_store=float(answer)
            else:
                memory_store=memory_store
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'operation':operation,'value':value}
                var_json=str(var_used)
                if new_conn:
                    try:
                        cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                        result = cur.fetchone()
                        if (result[-1] == operation_date):
                            operations_count=result[0] + 1
                            cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Computation Store',))
                            result=cur.fetchall()
                            operations_track['add_subtract_Store']=result[-1][2] + 1
                        new_conn=False
                    except:
                        print("Unable to query the database\n")
                    cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Computation Store', operations_track['add_subtract_Store'], var_json, memory_store, memory_store, time))
                    con.commit()
                    operations_count+=1



def query_by_Date():
    global memory_store, operations_count, logpath
    print("You have selected the report generation operation.\n")

    while True:
        query_date=str(raw_input('Please enter the date in the format YYYY-MM-DD\n'))
        if(re_Check(query_date)==0):
            break
    
    with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            cur.execute("select * from Calculations where Date(Executed) = Date(?)",(query_date,))
            #cur.execute("select * from Calculations where Operation=?",('Add',))
            rows = cur.fetchall()
            if not rows:
                print("No records were found for this date : {0}\n".format(query_date))
                return
        
            try:
                if not os.path.exists(logpath):
                    os.makedirs(logpath)
            except Exception as e:
                print("Unable to create ./reports folder\n")
            
            try:
                filepath=logpath + query_date + ".csv"


                with open(filepath, 'w') as file:
                    csv_writer=csv.writer(file, delimiter=';')
                    csv_writer.writerow(['Id','Operation','Count','Variables','Result','MR','Executed'])
                    for row in rows:
                        csv_writer.writerow(row)
                        #og.write("%s\n" % item)
                print("Successfully generated report file.\n")
            except IOError as e:
                print("Unable to create file for the operation\n")
            con.commit()



def query_by_range_Date():
    global memory_store, operations_count, logpath
    print("You have selected the report generation operation.\n")

    while True:
        query_date1=str(raw_input('Please enter the start date in the format YYYY-MM-DD\n'))
        if(re_Check(query_date1)==0):
            break

    while True:
        query_date2=str(raw_input('Please enter the end date in the format YYYY-MM-DD\n'))
        if(re_Check(query_date2)==0):
            break
    
    with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            cur.execute("select * from Calculations where Date(Executed) between Date(?) and Date(?)",(query_date1,query_date2,))
            #cur.execute("select * from Calculations where Operation=?",('Add',))
            rows = cur.fetchall()
            if not rows:
                print("No records were found for the specified dates : {0} - {1}\n".format(query_date1, query_date2))
                return
        
            try:
                if not os.path.exists(logpath):
                    os.makedirs(logpath)
            except Exception as e:
                print("Unable to create ./reports folder\n")
            try:
                filepath=logpath + query_date1 + "_" + query_date2 + ".csv"

                with open(filepath, 'w') as file:
                    csv_writer=csv.writer(file, delimiter=';')
                    csv_writer.writerow(['Id','Operation','Count','Variables','Result','MR','Executed'])
                    for row in rows:
                        csv_writer.writerow(row)
                        #og.write("%s\n" % item)
                print("Successfully generated report file.\n")
            except IOError as e:
                print("Unable to create file for the operation\n")
            con.commit()



def calculator_Operation(argument):
    global test_mode,operations_count, memory_store, last_operation_date, new_conn
    # Get the function from Operation_Dict dictionary
    func = Operation_Dict.get(argument, "Enter a valid number\n")
    # Execute the function
    test_mode=False
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
21: add_subtract_Store,
22: query_by_Date,
23: query_by_range_Date}



'''
Dictionary to keep a track of no.of operations requested per day for each type.
'''
operations_track={'addition':0,
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
This function prompts the user for an input for the desired operation.
'''
def main():

    print("Refer to the below menu for desired operation:\n+++++++++++++++++++++++++++++++++++++++++\n"\
        "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Cubic Root\n"\
            "7. Factorial\n8. Power\n9. Modulus\n10. Length of a Vector\n11. Cosine of an angle (radians/degrees)\n"
                "12. Sine of an angle (radians/degrees)\n13. Tan of an angle (radians/degrees)\n"
                    "14. Inverse cosine\n15. Inverse sine\n16. Inverse tan\n17. Logarathmic\n"
                        "18. Store a value in memory register.\n19. Display the value stored in memory register.\n"
                        "20. Remove the value stored in memory register.\n21. Use stored value for calculations\n"
                "22. Generate reports for given day.\n23. Generate reports within the given dates.\n"\
                    "+++++++++++++++++++++++++++++++++++++++++\n\n")

    global Operation_Dict
    while True:
        user_input=int(raw_input('Press the asscoiated number for the desired operation\n'))
        if user_input>23:
            print("Please enter number within the range 1-23.\n")
            continue
        calculator_Operation(user_input)


if __name__=="__main__":
    print("Welcome to a simple yet powerful calculator by Megasoft.\n")
    main()