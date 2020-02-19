#!/usr/local/bin/python3
import cgi

form = cgi.FieldStorage()
form_name = form.getvalue("name")

html = """
<html>
    <head>
       <title>Your Name is ...</title>
       <link href="https://fonts.googleapis.com/css?family=Lacquer&display=swap" rel="stylesheet">
       <link rel="stylesheet" href="../style.css">
    </head>
    <body>
        <h1>
            %s
        </h1>
    </body>
</html>
"""%form_name

print(html)

