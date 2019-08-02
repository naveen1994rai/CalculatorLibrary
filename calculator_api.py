#!/usr/bin/ python


'''
TO-DO
Code cleaning
'''




from flask import (Flask, jsonify, request, abort, render_template)
import math
from collections import OrderedDict
import re
import csv
import json
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
'add_sub_Store':0}





try:
    con = lite.connect('calc.db')
    cur = con.cursor()  
    cur.execute('SELECT SQLITE_VERSION()')
    
    cur.execute("CREATE TABLE IF NOT EXISTS Calculations(Id INT, Operation TEXT, Count INT, Variables TEXT, MR REAL, Executed TEXT)")
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
    global Operations_count, Memory_store
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
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Add', Operations_track['addition'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            #cur.execute("INSERT INTO Calculations VALUES(Operations_count, 'Add', 1, datetime('now','localtime')")
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sub', methods=['POST'])
def sub_args():
    global Operations_count, Memory_store
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
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Sub', Operations_track['subtraction'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/mul', methods=['POST'])
def mul_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 * arg2
            Operations_track['multiplication']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Mul', Operations_track['multiplication'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/div', methods=['POST'])
def div_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 / arg2
            Operations_track['division']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Div', Operations_track['division'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/sqrt', methods=['POST'])
def sqrt_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            answer = round(math.sqrt(abs(float(arg))),2)
            Operations_track['sqrt']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Sqrt', Operations_track['sqrt'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/crt', methods=['POST'])
def crt_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            arg=abs(float(arg))
            answer = round((arg)**(1./3.),3)
            Operations_track['crt']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Crt', Operations_track['crt'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)



@app.route('/factorial', methods=['POST'])
def factorial_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            arg=abs(int(arg))
            answer = math.factorial(arg)
            Operations_track['factorial']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Factorial', Operations_track['factorial'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/power', methods=['POST'])
def power_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = float(arg1) ** float((arg2))
            Operations_track['power']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'number':arg1,'power':arg2}
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Power', Operations_track['power'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/modulus', methods=['POST'])
def modulus_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = abs(int(arg1)) % abs(int(arg2))
            Operations_track['modulus']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Modulus', Operations_track['modulus'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/vector_Length', methods=['POST'])
def vector_Length_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = round(math.sqrt((abs(int(arg1)) ** 2) + (abs(int(arg2) ** 2))),2)
            Operations_track['vector']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Vector', Operations_track['vector'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/cos', methods=['POST'])
def cos_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
            answer=round(math.cos(float(arg1)),2)
            Operations_track['cos']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'angle':arg1,'format':arg}
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Cos', Operations_track['cos'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sin', methods=['POST'])
def sin_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
            answer=round(math.sin(float(arg1)),2)
            Operations_track['sin']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'angle':arg1,'format':arg}
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Sin', Operations_track['sin'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/tan', methods=['POST'])
def tan_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
            answer=round(math.tan(float(arg1)),2)
            Operations_track['tan']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'angle':arg1,'format':arg}
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Tan', Operations_track['tan'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/acos', methods=['POST'])
def acos_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.acos(value)
            Operations_track['acos']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Acos', Operations_track['acos'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)



@app.route('/asin', methods=['POST'])
def asin_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.asin(value)
            Operations_track['asin']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Asin', Operations_track['asin'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)


@app.route('/atan', methods=['POST'])
def atan_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.atan(value)
            Operations_track['atan']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Atan', Operations_track['atan'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)



@app.route('/log', methods=['POST'])
def log_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        number = request.json['number']
        base = request.json['base']
        if(re_Check(str(number))==0 and re_Check(str(base))==0):

            answer = math.log(float(number),int(base))
            Operations_track['log']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'number':number,'base':base}
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Log', Operations_track['log'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/var_Remove', methods=['POST'])
def var_Remove_args():
    global Operations_count, Memory_store
    try:
            Memory_store=None
            Operations_track['var_Remove']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=None
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Clear Memory', Operations_track['var_Remove'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':'cleared memory register'}), 200)
    except KeyError:
        abort(400)



@app.route('/var_Store', methods=['POST'])
def var_Store_args():
    global Operations_count, Memory_store
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0):

            Memory_store = value
            Operations_track['var_Store']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Store Value', Operations_track['var_Store'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':Memory_store,'status':'successfully stored new value'}), 200)
    except KeyError:
        abort(400)


@app.route('/print_Store', methods=['GET'])
def print_Store_args():
    global Memory_store, Operations_count
    try:
        Operations_track['print_Store']+=1
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=None
            var_json=json.dumps(var_used)
            cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Dsiplay MR', Operations_track['print_Store'], var_json, Memory_store, time))
            con.commit()
            Operations_count+=1
        return (jsonify({'answer':Memory_store}), 200)
    except KeyError:
        abort(400)





@app.route('/query_by_Date', methods=['POST'])
def query_by_Date():
    global Memory_store, Operations_count
    if not request.json:
        abort(400)
    try:
        query_date=request.json['date']
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            cur.execute("select * from Calculations where Date(Executed) = Date(?)",(query_date,))
            #cur.execute("select * from Calculations where Operation=?",('Add',))
            rows = cur.fetchall()
            if not rows:
                return (jsonify({'response':'no records found for this date'}), 400)
            
            try:

                with open("./check_report.csv", 'w') as file:
                    csv_writer=csv.writer(file, delimiter=';')
                    csv_writer.writerow(['Id','Operation','Count','Variables','MR','Executed'])
                    for row in rows:
                        csv_writer.writerow(row)
                        #og.write("%s\n" % item)
            except IOError as e:
                return (jsonify({'response':'unable to create file'}), 400)
            con.commit()
        return (jsonify({'answer':'file successfully created'}), 200)
    except KeyError:
        abort(400)



@app.route('/query_by_range_Date', methods=['POST'])
def query_by_range_Date():
    global Memory_store, Operations_count
    if not request.json:
        abort(400)
    try:
        query_date1=request.json['start']
        query_date2=request.json['end']
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            cur.execute("select * from Calculations where Date(Executed) between Date(?) and Date(?)",(query_date1,query_date2,))
            #cur.execute("select * from Calculations where Operation=?",('Add',))
            rows = cur.fetchall()
            if not rows:
                return (jsonify({'response':'no records found for this date'}), 400)
            
            try:

                with open("./check_report.csv", 'w') as file:
                    csv_writer=csv.writer(file, delimiter=';')
                    csv_writer.writerow(['Id','Operation','Count','Variables','MR','Executed'])
                    for row in rows:
                        csv_writer.writerow(row)
                        #og.write("%s\n" % item)
            except IOError as e:
                return (jsonify({'response':'unable to create file'}), 400)
            con.commit()
        return (jsonify({'answer':'file successfully created'}), 200)
    except KeyError:
        abort(400)










@app.route('/add_sub_Store', methods=['POST'])
def add_sub_Store_args():
    global Memory_store,Operations_count
    try:
        operation = request.json['operation']
        value = request.json['value']
        if(re_Check(str(operation))==0 and re_Check(str(value))==0):
            if operation=="add":
                answer=float(Memory_store) + float(value)
            elif operation=="sub":
                answer=float(Memory_store) - float(value)
            Operations_track['add_sub_Store']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'operation':operation,'value':value}
                var_json=json.dumps(var_used)
                cur.execute("insert into Calculations values (?,?,?,?,?,?)", (Operations_count, 'Computation Store', Operations_track['add_sub_Store'], var_json, Memory_store, time))
                con.commit()
                Operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)




if __name__ == "__main__":
    
    app.run(debug=True)
