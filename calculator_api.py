#!/usr/bin/ python

from flask import (Flask, jsonify, request, abort, render_template)
import math
import re

app = Flask(__name__)

Memory_store=""


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
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 + arg2
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)


@app.route('/sub', methods=['POST'])
def sub_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        if(re_Check(str(arg1))==0 and re_Check(str(arg2))==0):

            answer = arg1 - arg2
            return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/mul', methods=['POST'])
def mul_args():
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
            return (jsonify({'answer':Memory_store}), 200)
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
