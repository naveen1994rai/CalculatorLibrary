#!/usr/bin/ python


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

memory_store=""
operations_count=1
dateformat = '%Y-%m-%d'
last_operation_date=time.strftime(dateformat)
con=None
operations_track = OrderedDict()
new_conn=True

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
'add_sub_Store':0}


try:
    con = lite.connect('calc.db')
    cur = con.cursor()  
    cur.execute('SELECT SQLITE_VERSION()')
    
    cur.execute("CREATE TABLE IF NOT EXISTS Calculations(Id INT, Operation TEXT, Count INT, Variables TEXT, Result REAL, MR REAL, Executed TEXT)")

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



'''
This API accepts requests via CLI (curl) and browser.
'''

@app.route('/add', methods=['GET'])
def add_args():
    global operations_count, memory_store, last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    
    if request.json:
        #abort(400)
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        pass
    else:
        arg1 = float(request.args.get('argument1',0))
        arg2 = float(request.args.get('argument2',0))
        pass

    
    try:
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 + arg2
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['addition']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['addition']+=1

            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Add', operations_track['addition'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            #cur.execute("INSERT INTO Calculations VALUES(operations_count, 'Add', 1, datetime('now','localtime')")
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sub', methods=['POST'])
def sub_args():
    global operations_count, memory_store, last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 - arg2
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['subtraction']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['subtraction']+=1

            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Sub', operations_track['subtraction'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/mul', methods=['POST'])
def mul_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 * arg2
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['multiplication']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['multiplication']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Mul', operations_track['multiplication'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/div', methods=['POST'])
def div_args():
    global operations_count, memory_store, last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 / arg2
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['division']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['division']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Div', operations_track['division'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sqrt', methods=['POST'])
def sqrt_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg = request.json['value']
        if(re_Check(str(arg))==0):

            answer = round(math.sqrt(abs(float(arg))),2)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['sqrt']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['sqrt']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Sqrt', operations_track['sqrt'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/crt', methods=['POST'])
def crt_args():
    global operations_count, memory_store, last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg = request.json['argument1']
        if(re_Check(str(arg))==0):

            arg=abs(float(arg))
            answer = round((arg)**(1./3.),3)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['crt']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['crt']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Crt', operations_track['crt'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/factorial', methods=['POST'])
def factorial_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg = request.json['value']
        if(re_Check(str(arg))==0):

            arg=abs(int(arg))
            answer = math.factorial(arg)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['factorial']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['factorial']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Factorial', operations_track['factorial'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/power', methods=['POST'])
def power_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = float(arg1) ** float((arg2))
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['power']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['power']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'number':arg1,'power':arg2}
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Power', operations_track['power'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/modulus', methods=['POST'])
def modulus_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = abs(int(arg1)) % abs(int(arg2))
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['modulus']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['modulus']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Modulus', operations_track['modulus'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/vector_Length', methods=['POST'])
def vector_Length_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = round(math.sqrt((abs(int(arg1)) ** 2) + (abs(int(arg2) ** 2))),2)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['vector']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['vector']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[arg1,arg2]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Vector', operations_track['vector'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/cos', methods=['POST'])
def cos_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
            answer=round(math.cos(float(arg1)),2)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['cos']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['cos']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'angle':arg1,'format':arg2}
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Cos', operations_track['cos'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sin', methods=['POST'])
def sin_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
            answer=round(math.sin(float(arg1)),2)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['sin']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['sin']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'angle':arg1,'format':arg2}
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Sin', operations_track['sin'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/tan', methods=['POST'])
def tan_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['angle']
        arg2 = request.json['format']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):
            if arg2=="degrees":
                arg1=float((math.pi/180)*(float(arg1)))
            answer=round(math.tan(float(arg1)),2)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['sin']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['sin']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'angle':arg1,'format':arg2}
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Tan', operations_track['tan'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1

            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/acos', methods=['POST'])
def acos_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.acos(value)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['acos']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['acos']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Acos', operations_track['acos'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)



@app.route('/asin', methods=['POST'])
def asin_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.asin(value)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['asin']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['asin']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Asin', operations_track['asin'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)


@app.route('/atan', methods=['POST'])
def atan_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0 ):
            
            value=float(value)
            answer=math.atan(value)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['atan']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['atan']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Atan', operations_track['atan'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1

            return (jsonify({'answer':answer,'format':'radians'}), 200)
    except KeyError:
        abort(400)


@app.route('/log', methods=['POST'])
def log_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        number = request.json['number']
        base = request.json['base']
        if(re_Check(str(number))==0 and re_Check(str(base))==0):

            answer = math.log(float(number),int(base))
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['log']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['log']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'number':number,'base':base}
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Log', operations_track['log'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/var_Remove', methods=['POST'])
def var_Remove_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    try:
            memory_store=None
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['var_Remove']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['var_Remove']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=None
                var_json=json.dumps(var_used)
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
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Clear Memory', operations_track['var_Remove'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':'cleared memory register'}), 200)
    except KeyError:
        abort(400)


@app.route('/var_Store', methods=['POST'])
def var_Store_args():
    global operations_count, memory_store,last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    if not request.json:
        abort(400)
    try:
        value = request.json['value']
        if(re_Check(str(value))==0):

            memory_store = value
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['var_Store']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['var_Store']+=1
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used=[value]
                var_json=json.dumps(var_used)
                if new_conn:
                    try:
                        cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                        result = cur.fetchone()
                        if (result[-1] == operation_date):
                            operations_count=result[0] + 1
                            cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Store Value',))
                            result=cur.fetchall()
                            operations_track['var_Store']=result[-1][2] + 1
                        new_conn=False
                    except:
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Store Value', operations_track['var_Store'], var_json, memory_store, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':memory_store,'status':'successfully stored new value'}), 200)
    except KeyError:
        abort(400)


@app.route('/print_Store', methods=['GET'])
def print_Store_args():
    global memory_store, operations_count, last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    try:
        if (operation_date != last_operation_date):
            operations_count=1
            for k,v in operations_track.items():
                operations_track[k]=0
            operations_track['print_Store']+=1
            last_operation_date = operation_date
        elif (operation_date == last_operation_date):
            operations_track['print_Store']+=1
        with lite.connect("calc.db") as con:
            cur = con.cursor()
            time = datetime.now().strftime('%Y-%m-%d')
            var_used=None
            var_json=json.dumps(var_used)
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
                        pass
            cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Dsiplay MR', operations_track['print_Store'], var_json, memory_store, memory_store, time))
            con.commit()
            operations_count+=1
        return (jsonify({'answer':memory_store}), 200)
    except KeyError:
        abort(400)


@app.route('/add_sub_Store', methods=['POST'])
def add_sub_Store_args():
    global memory_store,operations_count, last_operation_date, new_conn
    operation_date= datetime.now().strftime(dateformat)
    try:
        operation = request.json['operation']
        value = request.json['value']
        if(re_Check(str(operation))==0 and re_Check(str(value))==0):
            if operation=="add":
                answer=float(memory_store) + float(value)
            elif operation=="sub":
                answer=float(memory_store) - float(value)
            if (operation_date != last_operation_date):
                operations_count=1
                for k,v in operations_track.items():
                    operations_track[k]=0
                operations_track['add_sub_Store']+=1
                last_operation_date = operation_date
            elif (operation_date == last_operation_date):
                operations_track['add_sub_Store']+=1
            
            with lite.connect("calc.db") as con:
                cur = con.cursor()
                time = datetime.now().strftime('%Y-%m-%d')
                var_used={'operation':operation,'value':value}
                var_json=json.dumps(var_used)
                if new_conn:
                    try:
                        cur.execute("SELECT * FROM Calculations ORDER BY Id DESC LIMIT 1")
                        result = cur.fetchone()
                        if (result[-1] == operation_date):
                            operations_count=result[0] + 1
                            cur.execute("SELECT * FROM Calculations WHERE Operation = (?)",('Computation Store',))
                            result=cur.fetchall()
                            operations_track['add_sub_Store']=result[-1][2] + 1
                        new_conn=False
                    except:
                        pass
                cur.execute("insert into Calculations values (?,?,?,?,?,?,?)", (operations_count, 'Computation Store', operations_track['add_sub_Store'], var_json, answer, memory_store, time))
                con.commit()
                operations_count+=1
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/query_by_Date', methods=['POST'])
def query_by_Date():
    global memory_store, operations_count
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
                return (jsonify({'response':'unable to create file','error':e}), 400)
            con.commit()
        return (jsonify({'answer':'file successfully created'}), 200)
    except KeyError:
        abort(400)


@app.route('/query_by_range_Date', methods=['POST'])
def query_by_range_Date():
    global memory_store, operations_count
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


if __name__ == "__main__":
    app.run(debug=True)
