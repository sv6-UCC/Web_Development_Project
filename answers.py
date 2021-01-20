#!/usr/local/bin/python3
from cgitb import enable
enable()
from cgi import FieldStorage
from html import escape
from time import strptime
import pymysql as db
print('Content-Type: text/html')
print()

form_data =FieldStorage()
bandname =''
gig_date =''
result =''
if len(form_data) > 0:
    try:
        bandname = escape(form_data.getfirst('bandname', '').strip())
        gig_date = escape(form_data.getfirst('gig_date', '').strip())
        if bandname or gig_date:
            connection = db.connect('cs1.ucc.ie', 'sv6', 'oguri', 'cs6503_cs1106_sv6')
            cursor = connection.cursor(db.cursors.DictCursor)
            if bandname:
                cursor.execute("""SELECT * FROM gigs
                                  WHERE bandname = %s""", (bandname))
                if cursor.rowcount == 0:
                    result = """<p>Unknown band name</p>"""
            if gig_date:
                try:
                    valid_date = strptime(gig_date, '%Y-%m-%d')
                except ValueError:
                    result+= """<p>Illegal date </p>"""

            if result == '':
                if bandname and not gig_date:
                    cursor.execute("""SELECT * FROM gigs
                                      WHERE bandname = %s""", (bandname))
                elif gig_date and not bandname:
                    cursor.execute("""SELECT * FROM gigs
                                      WHERE gig_date >= %s""", (gig_date))
                else:
                    cursor.execute("""SELECT * FROM gigs
                                      WHERE gig_date >= %s
                                      AND bandname =%s""", (gig_date,bandname))
                result = '<table>'
                result += '<caption> gigs </caption>'
                result += '<tr><th>num</th><th>bandname</th><th>date</th></tr>''
                for row in cursor.fetchall():
                    result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (row ['num'],row['bandname'], row['gig_date'])
                result+= '</table>'
            connection.commit()
            cursor.close()
            connection.close()
    except (db.Error):
        result ="""<p>Apolgies there has been a problem</p>"""
print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Our Gigs</title>
</head>
<body>
<form action="answers.py" method="get">
<label>Band name: </label>
<input type="text" name="bandname" value="%s" />
<label>Gig date (YYYY-MM-DD): </label>
<input type="text" name="gig_date" value="%s" />
<input type="submit" value="Search for gigs" />
</form>
%s
</body>
</html>""" % (bandname, gig_date, result))
