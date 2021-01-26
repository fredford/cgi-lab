#!/usr/bin/env python3
import os
import json
import cgi
import cgitb
import webbrowser
import templates
import sys
import requests


cgitb.enable()
#form = cgi.FieldStorage()

#print(json.dumps(dict(os.environ)))
#print(cgi.print_environ())

#print(os.environ['QUERY_STRING'])

#print(os.environ.keys())

print("""
<html>
<body>
<h1> Hello world</h1>
""")
print(f"<p>QUERY_STRING= {os.environ['QUERY_STRING']}</p>")
if "HTTP_USER_AGENT" in os.environ:
    print(f"<p>BROWSER={os.environ['HTTP_USER_AGENT']}</p>")

print("<ul>")


for parameter in os.environ['QUERY_STRING'].split('&'):
    (name, value) = parameter.split('=')
    print(f"<li><em>{name}</em> = {value}</li>")
print("""
</ul>
""")

print("""
</ul>
""")

print(f"""
{templates.login_page()}
""")

posted_bytes = os.environ['CONTENT_LENGTH']
print(f"<p>POSTED={posted_bytes}</p>")

if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")

print("""
</body>
</html>
""")


def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(r"""
    <h1> Welcome! </h1>

    <form method="POST" action="hello.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)