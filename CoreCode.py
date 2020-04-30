from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3 as sql
import hashlib
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request

@app.route('/')
def student():
   return render_template('final.html')

@app.route('/success',methods = ['POST', 'GET'])
def success():
   if request.method == 'POST':
      result = request.form
      conn = sql.connect('static/main.db')
      cursor = conn.cursor()
      username = request.form.get('username')
      password = request.form.get('password')
      cursor.execute("SELECT * FROM `student_table` WHERE `username` = ? AND `password` = ?", (username, password))
      if cursor.fetchone() is not None:

         #engine.say('Hello User')
         #engine.say('Welcome to Web portal')
         #engine.runAndWait()
         return render_template("articlesmodified1.html")
