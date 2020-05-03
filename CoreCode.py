from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3 as sql
import hashlib
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request

@app.route('/')
def student():
   return render_template('Login.html')

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
      
@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/iv')
def iv():
   global topic
   topic = "iv"
   return render_template('iv.html')

@app.route('/ke')
def ke():
   global topic
   topic = "ke"
   return render_template('ke.html')

@app.route('/acc')
def acc():
   global topic
   topic = "acc"
   return render_template('acc.html')

@app.route('/ia')
def ia():
   global topic
   topic = "ia"
   return render_template('ia.html')

@app.route('/rv')
def rv():
   global topic
   topic = "rv"
   return render_template('rv.html')

@app.route('/cloud_article')
def cloud_article():
    return render_template('cloud_article.html')

@app.route('/questions')
def questions():
   global topic
   topic = "questions"
   return render_template('questions.html')

@app.route('/questions1')
def questions1():
   global topic
   topic = "questions1"
   return render_template('questions1.html')

@app.route('/questions2')
def questions2():
   global topic
   topic = "questions2"
   return render_template('questions2.html')

@app.route('/questions3')
def questions3():
   global topic
   topic = "questions3"
   return render_template('questions3.html')

@app.route('/questions4')
def questions4():
   global topic
   topic = "questions4"
   return render_template('questions4.html')

