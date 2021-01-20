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
attempt2 =''
result = ''
javascript =''
colour_button =''
paragraph=""
score =0
if len(form_data) != 0:
    attempt = escape(form_data.getfirst('guess', '').strip())
    attempt2 = escape(form_data.getfirst('guess2', '').strip())
    attempt3 = escape(form_data.getfirst('guess3', '').strip())
    attempt4 = escape(form_data.getfirst('guess4', '').strip())
    attempt5 = escape(form_data.getfirst('guess5', '').strip())
    try:
        if attempt == "A":
            score +=1
        if attempt2 == "10":
            score+=1
        if attempt3 == "truth":
            score+=1
        if attempt4 == "2004":
            score +=1
        if attempt5 == "head":
            score+=1
        if score == 0:


            result ="""<section><p id ="yes2">Well done you scored 0 out of 5</p>
                       <p> <a href ="finished.html">Click here to continue</a></p></section>"""
        if score == 1:
            result ="""<section><p id ="yes2">Well done you scored 1 out of 5</p>
                       <p> <a href ="finished.html">Click here to continue</a></p></section>"""
        if score == 2:
            result ="""<section><p id ="yes2">Well done you scored 2 out of 5</p>
                       <p> <a href ="finished.html">Click here to continue</a></p></section>"""
        if score == 3:
            result ="""<section><p id ="yes2">Well done you scored 3 out of 5</p>
                       <p> <a href ="finished.html">Click here to continue</a></p></section>"""
        if score == 4:
            result ="""<section><p id ="yes2">Well done you scored 4 out of 5</p>
                       <p> <a href ="finished.html">Click here to continue</a></p></section>"""
        if score == 5:
            result ="""<section><p id ="yes2">Well done you scored 5 out of 5</p>
                       <p> <a href ="finished.html">Click here to continue</a></p></section>"""
        javascript ="""<script src='q1.js' rel='module'></script>"""
        colour_button="""<section id ="yes3"><h1>Answers</h1><p>Click the skull to reveal the answers </p>
                         <img id ="man" src="skull2.png"
                         alt="Mute button"/></section>"""

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
            <link rel='stylesheet' href='quiz.css' />
            <title>Zombie Mayhem</title>
        </head>
        <body>
            <header>
             <h1> Zombie Mayhem</h1>


           </header>

        <main>
        <section>
        <p>Welcome to my Zombie quiz.Try your best to answer these 5 questions correctly. If you finish the quiz you might get a
        special suprise!!</p>
        </section>
            <form action="q1.py" method="post">
            <section>
            <img src="q1_image.jpg"
                 alt="World Zombie Day"
                 height ="250" width ="450"/>
            <p> Q1 What date was World Zombie Day 2019 in London? </p>
                <label for="A">A:October 5th </label>
                <input type="radio" name="guess" id="A" value="A" />
                <label for="B">B:October 8th: </label>
                <input type="radio" name="guess" id="B" value ="B" />
                <label for="C">C:October 12th: </label>
                <input type="radio" name="guess" id="C" value ="C"/>

            </section>
            <section>
            <img src="q2_image.jpg"
                 alt="Walking Dead Poster"
                 height ="250" width ="450"/>
            <p> Q2 As of April 2020.How many seasons does The Walking Dead have? </p>
            <label for="8">A:8:</label>
            <input type="radio" name="guess2" id="8" value="8" />
            <label for="9">B:9 </label>
            <input type="radio" name="guess2" id="9" value ="9" />
            <label for="10">C:10</label>
            <input type="radio" name="guess2" id="10" value ="10"/>

            </section>

            <section>
            <img src="q3_image.jpeg"
                 alt="NZAMBIII"
                 height ="250" width ="350"/>
            <p> Q3 True or False. The word zombie is related to the African word nzambi, which means god. </p>
            <label for="truth">A:True:</label>
            <input type="radio" name="guess3" id="truth" value="truth" />
            <label for="lie">B:False </label>
            <input type="radio" name="guess3" id="lie" value ="lie" />
            </section>

            <section>
            <img src="q4_image.jpg"
                 alt="Shaun of the Dead poster"/>
            <p> Q4 In what year did the zombie movie Shaun of the Dead release in theaters?  </p>
            <label for="2002">A:2002:</label>
            <input type="radio" name="guess4" id="2002" value="2002" />
            <label for="2003">B:2003 </label>
            <input type="radio" name="guess4" id="2003" value ="2003" />
            <label for="2004">C:2004 </label>
            <input type="radio" name="guess4" id="2004" value ="2004" />
            </section>

            <section>
            <img src="q5_image.jpg"
                alt="Another Zombie"
                height ="250" width ="450"/>
            <p> Q5 According to zombie folklore. What is the most effective way of killing a zombie?</p>
            <label for="head">A:Damage its head:</label>
            <input type="radio" name="guess5" id="head" value="head" />
            <label for="heart">B:Damage its heart</label>
            <input type="radio" name="guess5" id="heart" value ="heart" />
            <label for="legs">C:Damage its legs</label>
            <input type="radio" name="guess5" id="legs" value ="legs" />
            <input id = "enter" type="submit" value="Submit"/>
            </section>
            </form>



         %s
         %s
        </main>
        </body>

    </html>""" % (javascript,result,colour_button))
