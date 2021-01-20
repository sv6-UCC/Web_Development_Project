#!/usr/local/bin/python3
from cgitb import enable
enable()
from cgi import FieldStorage
from html import escape
from time import strptime
import pymysql as db

print('Content-Type: text/html')
print()
form_data = FieldStorage()
student_ids =""
lect_date =""
if len(form_data) > 0:
    try:
        student_ids = escape(form_data.getfirst('student_ids', '').strip())
        lect_date = escape(form_data.getfirst('lect_date', '').strip())
        if student_ids or lect_date:
            connection = db.connect('my_server', 'me', 'my_password', 'my_db')
            cursor = connection.cursor(db.cursors.DictCursor)
            if student_ids:
                try:
                    real_id =int(student_ids)
                except:
                    outcome += """<p>Student Id must be an integer</p>"""

            if lect_date:
                try:
                    valid_date = strptime(lect_date, '%Y-%m-%d')
                except ValueError:
                    outcome+= """<p>Illegal date </p>"""
            if outcome =='':
                if student_ids and not lect_date:
                    cursor.execute("""SELECT * FROM students
                                      WHERE student_id = %i""", (student_ids))
                    if cursor.rowcount == 0:
                        outcome = """<p>This student is not in the database</p>"""
                if lect_date and not student_ids:
                    cursor.execute("""SELECT * FROM attendance
                                      WHERE lect_date = %s""", (lect_date))
                    if cursor.rowcount > 0:
                        outcome = """<p>This student's attendance is already in the database</p>"""
                else:
                    cursor.execute("""INSERT INTO attendance (lect_date, student_id)
                                      VALUES (%s, %s)""", (lect_date, student_ids))
                    outcome ="<p>Succesfully Inserted</p>"
            connection.commit()
            cursor.close()
            connection.close()
    except (db.Error):
        outcome ="<p>There has been an error</p>"

print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Lecture Attendance</title>
</head>
<body>
%s
</body>
</html>""" % (outcome))
