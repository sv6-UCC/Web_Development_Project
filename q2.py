#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie


form_data = FieldStorage()
attempt = ''
result = ''
javascript =''
score = escape(form_data.getfirst('score', '').strip())
if len(form_data) != 0:
    attempt = escape(form_data.getfirst('guess', '').strip())
    if not attempt:
        result ="<p>Please select either A,B or C "
    else:
        try:
            if attempt == "A":
                result ="""<p id ="yes">Correct</p>"""
                javascript ="""<script src='q1.js' rel='module'></script>"""
            if attempt == "B":
                result ="<p>Incorrect</p>"
                javascript ="""<script src='q1.js' rel='module'></script>"""
            if attempt == "C":
               result ="<p>Incorrect</p>"
               javascript ="""<script src='q1.js' rel='module'></script>"""
        except:
            result = "<p>Sorry we are experiencing problems please contact later</p>"






print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />

            %s
            <link rel='stylesheet' href='menu.css' />
            <title>Zombie Mayhem</title>
        </head>
        <body>
            <form action="q2.py" method="post">
            <p> What day is World Zombie Day? </p>
                <label for="A">A:October 8th </label>
                <input type="radio" name="guess" id="A" value="A" />
                <label for="B">B:October 12th: </label>
                <input type="radio" name="guess" id="B" value ="B" />
                <label for="C">C:October 18th: </label>
                <input type="radio" name="guess" id="C" value ="C"/>
                <input id = "enter" type="submit" value="Submit" />
            </form>


        </body>
        <p> Score so far:%s </p>
        <canvas  width='200' height='80'></canvas>
        %s
    </html>""" % (javascript,score,result))
