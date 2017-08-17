#!/usr/bin/env python 

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import sys
import csv   

app = Flask(__name__)

barcodes = []

open('list.csv', 'w').close()#initializes list.csv file

def csvappend(string):
    print(string)
    with open('list.csv', 'a+') as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([string])

def csvretrieve():
    del barcodes[:]
    with open('list.csv', 'r') as f:
         reader = csv.reader(f, delimiter=',')
         for code in reader:
             barcodes.append(code[0])
    return(barcodes)

def csvclear():
    open('list.csv', 'w').close()

@app.route('/', methods =['GET'])
def index():
    #return str(barcodes)	
    #return  render_template('index.html', barcodes = barcodes)
    csvretrieve()
    return  render_template('index.html', barcodes = barcodes)

@app.route('/', methods =['POST'])
def parse_request(): 
    #data = request.args.to_dict()
    #print(data)
    #sys.stdout.flush()
    form = list(request.form.to_dict().keys())[0]
    print(form)
    sys.stdout.flush()
    print(type(form))
    sys.stdout.flush()
    csvappend(str(form))
    #barcodes.append(form)
    return str(form)

@app.route('/result', methods =['GET'])
def clearall():
    del barcodes[:]
    csvclear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
