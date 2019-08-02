#!/usr/bin/ python


'''
TO-DO
Include sql execution for each function
Generate reports based off date guven by the user
'''




from flask import (Flask, jsonify, request, abort, render_template)
import math
from collections import OrderedDict
import re
import sqlite3 as lite
import sys
from datetime import datetime
import time

app = Flask(__name__)

Memory_store=""
Operations_count=1

con=None
Operations_track = OrderedDict()

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





try:
    con = lite.connect('calc.db')
    cur = con.cursor()  
    cur.execute('SELECT SQLITE_VERSION()')
    
    cur.execute("CREATE TABLE IF NOT EXISTS Calculations(Id INT, Operation TEXT, Count INT, Date TEXT)")
    '''
    cur.execute("INSERT INTO Operations VALUES(1,'Add',2,datetime('now','localtime'))")
    
    cur.execute("INSERT INTO Users VALUES(2,'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3,'Greg')")
    
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    print(type(row))
    #print(data)
    #print("SQLite version: %s" % data)   
    '''              
except lite.Error as e:   
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:    
    if con:
        con.close()







def re_Check(string): 
  
    # Check for special characters exisitent in the input
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]') 
      
    # Pass the string in search method of the regex object.     
    if(regex.search(string) == None): 
        
        #print("Input is accepted\n") 
        return 0
          
    else: 
        #print("Input cannot contain any special characters i.e. [@_!#$%^&*()<>?/|}{~:]\tPlease enter again\n")
        return 1




@app.route('/')
def home_page():
    return 'Welcome to a simple yet powerful calculator by Megasoft'


@app.route('/add', methods=['POST'])
def add_args():
    global Operations_count
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 + arg2
            Operations_track['addition']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime("%d %B %Y")
                cur.execute("insert into Calculations values (?,?,?,?)", (Operations_count, 'Add', Operations_track['addition'], time))
                con.commit()
                Operations_count+=1
            #cur.execute("INSERT INTO Calculations VALUES(Operations_count, 'Add', 1, datetime('now','localtime')")
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sub', methods=['POST'])
def sub_args():
    global Operations_count
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 - arg2
            Operations_track['subtraction']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime("%d %B %Y")
                cur.execute("insert into Calculations values (?,?,?,?)", (Operations_count, 'Sub', Operations_track['addition'], time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/mul', methods=['POST'])
def mul_args():
    global Operations_count
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 * arg2
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/div', methods=['POST'])
def div_args():
    global Operations_count
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 / arg2
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/sqrt', methods=['POST'])
def sqrt_args():
    global Operations_count
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            answer = round(math.sqrt(abs(float(arg))),2)
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/crt', methods=['POST'])
def crt_args():
    global Operations_count
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            arg=abs(float(arg))
            answer = round((arg)**(1./3.),3)
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)



@app.route('/factorial', methods=['POST'])
def factorial_args():
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            arg=abs(int(arg))
            answer = math.factorial(arg)
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/power', methods=['POST'])
def power_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            arg=abs(int(arg))
            answer = float(base) ** float((power))
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/modulus', methods=['POST'])
def modulus_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = abs(int(arg1)) % abs(int(arg2))
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/vector_Length', methods=['POST'])
def vector_Length_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = round(math.sqrt((abs(int(arg1)) ** 2) + (abs(int(arg2) ** 2))),2)
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/cos', methods=['POST'])
def cos_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
                answer=round(math.cos(float(arg1)),2)
            elif arg2=="radians":
                answer=round(math.cos(float(arg1)),2)

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sin', methods=['POST'])
def sin_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
                answer=round(math.sin(float(arg1)),2)
            elif arg2=="radians":
                answer=round(math.sin(float(arg1)),2)

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/tan', methods=['POST'])
def tan_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
                answer=round(math.tan(float(arg1)),2)
            elif arg2=="radians":
                answer=round(math.tan(float(arg1)),2)

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/acos', methods=['POST'])
def acos_args():
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.acos(value)

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)



@app.route('/asin', methods=['POST'])
def asin_args():
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.asin(value)

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)


@app.route('/atan', methods=['POST'])
def atan_args():
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.atan(value)

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)



@app.route('/log', methods=['POST'])
def log_args():
    if not request.json:
        abort(400)
    try:
        number = request.json['number']
        base = request.json['base']
        if(re_Check(str(number))==0 and re_Check(str(base))==0):

            answer = math.log(float(number),int(base))
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/var_Remove', methods=['POST'])
def var_Remove_args():
    global Memory_store
    try:
            Memory_store=None
            return (jsonify({'answer':'cleared memory register'}), 200)
    except KeyError:
        abort(400)



@app.route('/var_Store', methods=['POST'])
def var_Store_args():
    global Memory_store
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0):

            Memory_store = value
            return (jsonify({'answer':Memory_store,'status':'successfully stored new value'}), 200)
    except KeyError:
        abort(400)


@app.route('/print_Store', methods=['POST'])
def print_Store_args():
    global Memory_store
    try:
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime("%d %B %Y")
            cur.execute("SELECT * FROM Calculations")
            rows = cur.fetchall()
            return_list=[]

            '''
            with open("./check_report.txt", 'a+') as log:
                for row in rows:
                    log.write(row)
            '''
            for row in rows:
                return_list.append(row)
            
            
            con.commit()
        return (jsonify({'answer':Memory_store,'table query':return_list}), 200)
    except KeyError:
        abort(400)



@app.route('/add_sub_Store', methods=['POST'])
def add_sub_Store_args():
    global Memory_store
    try:
        operation = request.json['operation']
        value = request.json['value']
        if(re_Check(str(operation))==0 and re_Check(str(value))==0):
            if operation=="add":
                answer=float(Memory_store) + float(value)
            elif operation=="sub":
                answer=float(Memory_store) - float(value)

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)




if __name__ == "__main__":
    
    app.run(debug=True)
