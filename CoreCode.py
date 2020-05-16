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

@app.route('/ia/nltkk',methods = ['POST', 'GET'])
def nltkk():
   if topic == "ia":
      if request.method == 'POST':
         user_text1 = request.form.get('user_text1')
         user_text2 = request.form.get('user_text2')
         user_text2 = str(user_text2)
         user_text1 = str(user_text1)
         
         WORD = re.compile(r'\w+')

         def get_cosine(vec1, vec2):
              intersection = set(vec1.keys()) & set(vec2.keys())
              numerator = sum([vec1[x] * vec2[x] for x in intersection])

              sum1 = sum([vec1[x]**2 for x in vec1.keys()])
              sum2 = sum([vec2[x]**2 for x in vec2.keys()])
              denominator = math.sqrt(sum1) * math.sqrt(sum2)
               
              if not denominator:
                 return 0.0
              else:
                 return float(numerator) / denominator
               
         text1 = 'A derivative is a contract between two parties which derives its value/price from an underlying asset. The most common types of derivatives are futures, options, forwards and swaps.'
         text2 = 'Average acceleration is the change in velocity divided by an elapsed time'

         vector1 = text_to_vector(text1)
         vector2 = text_to_vector(text2)

         uservector1= text_to_vector(user_text1)
         uservector2= text_to_vector(user_text2)

         def text_to_vector(text):
              words = WORD.findall(text)
              return Counter(words)
 
         av1 = get_cosine(uservector1, vector1)
         av2 = get_cosine(uservector2, vector2)
         print('Cosine:', av1)
         print('Cosine:', av2)

         #######Evaluating accuracy########
         if av1*100 > 40:
            #print("bright")
            ans1 = "bright"
