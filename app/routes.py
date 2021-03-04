"""Route declaration."""
from flask import current_app as app
from flask import render_template, url_for, redirect, Flask
from app.form import VehicleData
import pyodbc 
from .dataBase import DBHelper
import json
import collections


@app.route("/", methods=['GET', 'POST'])
def home():
    
    form = VehicleData()
    #defining the database instance
    db = DBHelper()
    nav = [
	    {"name": "Home", "url": url_for('home')},
		]
    #storingdata into the database
    if form.validate_on_submit():
        #user have add the data into database
        db._add(form)

        return redirect(url_for('home'))
        
   
    #getting data from dataBase
    cars = db._getData()
    j =json.loads(cars)

    return render_template(
        "home.html",
        form=form,
        nav=nav,
        cars=j,
        title="Stock Finder",
        description="List of cars on the table",
    )



