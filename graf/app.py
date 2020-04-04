from flask import Flask, render_template,request,session, url_for
import json
import urllib.request
import csv
import openpyxl
import pandas as pd 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import time
app = Flask(__name__)
@app.route("/")
def index():
    print('1')
    return render_template("home.html")

@app.route("/month", methods=['POST'])
def other():
    print('2')
    plt.clf()

    taxcut = request.form['income']
    liabilities= request.form['liabilities']
    nliabilities = request.form['negotiable']
    spend = request.form['noessentials']
    saved= request.form['saved']
    labels = 'Non-negotiable Liabilities', 'Negotiable Liabilities', 'Spent', 'Saved'
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    sizes = [int(liabilities),int(nliabilities),int(spend),int(saved)]
    plt.pie(sizes, colors=colors,
    autopct='%1.1f%%', shadow=True)
    plt.legend(labels, loc="best")
    plt.axis('equal')
    plt.title("Overview of how you spend your money")

    plt.savefig('static/foo100.png',dpi=100)
    
    plt.tight_layout()
    a = "It appears you are spending more then you sae this can be very dangerous"
    b= "It is suggested that you spend only 15% of your savings. "
    c = "And rember to spend after saving not save after spending."
    a1 = "It appears you are spending less then you save"
    c1="This is great and you are a step closer to financial freedom."
    a2= "It appears you are spending almost as much as you save"
    if int(saved)>int(spend):
        return render_template("other.html" ,spend=spend,saved=saved, a=a1,b=b,c1=c)
    elif int(saved)<int(spend):
        return render_template("other.html" ,spend=spend,saved=saved,a=a,b=b,c=c)
    else:
        return render_template("other.html" ,spend=spend,saved=saved,a=a2,b=b,c=c)



if __name__ == '__main__':
    app.run(debug=True)