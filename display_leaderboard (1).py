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
    cursor.execute("""SELECT candidate_name, total_votes 
                      FROM candidates 
                      ORDER BY total_votes DESC, candidate_name ASC""")
    result = '<table><tr><th>Candidate name</th><th>Total votes</th></tr>'
    for row in cursor.fetchall():
        result += '<tr><td>%s</td><td>%i</td></tr>' % (row['candidate_name'], row['total_votes'])
    result += '</table>'
    cursor.close()  
    connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
        
print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Leaderboard</title>
            </head>
            <body>
                %s
            </body>
            </html>""" % (result))
