#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

form_data = FieldStorage()
username = ''
result = ''
if len(form_data) != 0:
    username = escape(form_data.getfirst('username', '').strip())
    password1 = escape(form_data.getfirst('password1', '').strip())
    if not username and password1:
        result = '<p>Error: Username and password required </p>'
    else:
        try:
            connection = db.connect('cs1.ucc.ie', 'sv6', 'oguri', 'cs6503_cs1106_sv6')
            cursor = connection.cursor(db.cursors.DictCursor)
            sha256_password = sha256(password1.encode()).hexdigest()
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s
                              AND password =%s""", (username,sha256_password))
            if cursor.rowcount < 1:
                result = '<p>Error: Please enter a valid username and password</p>'
            else:
                cursor.execute("""UPDATE users u1 INNER JOIN users u2
                                  SET u2.score_input = u1.score_input
                                  WHERE u1.username ='default'
                                  AND u2.username =%s""",(username))

                connection.commit()
                cursor.close()
                connection.close()
                result = """
                <section>
                   <p>Succesfully inserted!</p>
                   <p>View the updated <a href ='leaderboard.py'>Leaderboard</a></p>
                   </section>"""


        except (db.Error, IOError):
            result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">

        <head>
            <meta charset="utf-8" />
            <link rel='stylesheet' href='menu.css' />
            <title>Zombie Mayhem</title>
        </head>

        <body>
        <main>
        <section>
            <p>Thank you for playing Zombie Mayhem.If you want to be on the leaderboard please enter your username
                and password below. Otherwise you can go back to the main menu or play the game again.</p>
            <p><strong>Warning</strong> If you have played this game more than once,only enter your username and password if your score is greater than
            your high score on the leaderboard.</p>
        </section>
        <nav>
             <ul>
                 <li><a href ="menu.html">Back to Main Menu</a></li>
                 <li><a href ="nice.html">Play Game</a></li>
             </ul>
        </nav>
            <form action="congratulations.py" method="post">
                <label for="username">User name: </label>
                <input type="text" name="username" id="username" value="%s" />
                <label for="password1">Password: </label>
                <input type="password" name="password1" id="password1" />
                <input type="submit" value="Submit" />
            </form>
            %s
        </main>
        </body>
    </html>""" % (username, result))
