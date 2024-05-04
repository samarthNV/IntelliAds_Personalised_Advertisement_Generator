import sqlite3
import os
from flask import Flask, render_template, request, redirect
from gemini_functions import *

app = Flask(__name__)


@app.route("/landing", methods=['GET', 'POST'])
def landing_site():
    return render_template('landing_page.html')


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':

        cust_name = request.form['customerName']
        cust_desc = request.form['customerInterests']
        product_name = request.form['productName']
        product_desc = request.form['productDetails']

        ans = answer_prompt_bard(create_prompt_from_description(
            product_name=product_name, product_desc=product_desc, customer_name=cust_name, customer_interests=cust_desc))
        return render_template('ad_display.html', advert=ans)

    return render_template('ad_generation_form.html')



if __name__ == '__main__':
    app.run(debug=True)
