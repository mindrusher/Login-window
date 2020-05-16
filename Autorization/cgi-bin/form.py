#!/usr/bin/env python3
import cgi
import html

from request import Request

req = Request()

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "")
text2 = form.getfirst("TEXT_2", "")
text1 = html.escape(text1)
text2 = html.escape(text2)

answer = req.get_log_pas(text1, text2)

print("Content-type: text/html\n")
print(answer)


