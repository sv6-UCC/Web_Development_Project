#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
import pymysql as db

print('Content-Type: text/html')
print()

result = ''
try:
    connection = db.connect('cs1.ucc.ie', 'sv6', 'oguri', 'cs6503_cs1106_sv6')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT username,score_input
                      FROM users
                      WHERE username <> 'default'
                      ORDER BY score_input DESC""")
    result = '<table><tr ><th>username</th><th>Score</th></tr>'
    for row in cursor.fetchall():
        result += '<tr><td>%s</td><td>%s</td></tr>' % (row['username'], row['score_input'])
    result += '</table>'
    cursor.close()
    connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <link rel='stylesheet' href='menu.css' />
                <title>Leaderboard</title>

            </head>
            <body>
            <nav>
            <ul>
            <li><a href ="menu.html">Back to Main Menu</a></li>
            <li><a href ="nice.html">Play Game</a></li>
            </ul>
            </nav>
                %s
            </body>
            </html>""" % (result))
