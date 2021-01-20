#!/usr/local/bin/python3

from datetime import datetime

print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Greetings!</title>
        </head>
        <body>
            <p>
                Hello world. It is %s, right now.
            </p>
        </body>
    </html>""" % (datetime.now().strftime('%H:%M:%S %d-%m-%y')))
