#!/usr/bin/env python 

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import sys

app = Flask(__name__)

barcodes = []

@app.route('/', methods =['GET'])
def index():
    #return str(barcodes)	
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
    barcodes.append(form)
    return str(form)

@app.route('/result', methods =['GET'])
def clearall():
    del barcodes[:]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
