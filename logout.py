#!/usr/local/bin/python3

from cgitb import enable
enable()

from os import environ
from shelve import open
from http.cookies import SimpleCookie

print('Content-Type: text/html')
print()

result = """<p>You are already logged out</p>
             <nav>
             <ul>
             <li><a href="menu.html">Main Menu</a></li>
             <li><a href="index.html">Index</a></li>
             </ul>
             </nav>"""

try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=True)
            session_store['authenticated'] = False
            session_store.close()
            result = """
                <p>You are now logged out. Thanks for using Zombie Mayhem</p>
                <nav>
                <ul>
                <li><a href="login.py">Login</a></li>
                <li><a href="index.html">Index</a></li>
                </ul>
                </nav>"""
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

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
            %s
        </main>
        </body>
    </html>""" % (result))
