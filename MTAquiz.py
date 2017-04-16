#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>MTA Subway Quiz</title>"
print "<head>"
print "<body>"

print "<h1>MTA Subway Quiz</h1>"
print "<form method=GET action=\"MTAquiz.cgi\">"

for i in range(1, 5):
    print "<p>Question %s: Which line stops at <strong>#</strong>?</p>" % i
    print "<input type=\"radio\" name=\"q%s\" value=\"1\">1<br>" % i
    print "<input type=\"radio\" name=\"q%s\" value=\"2\">2<br>" % i
    print "<input type=\"radio\" name=\"q%s\" value=\"3\">3<br>" % i
    print "<input type=\"radio\" name=\"q%s\" value=\"4\">4<br>" % i
    print "<input type=\"hidden\" name=\"s%s\" value=\"#\">" % i
    print "<input type=\"hidden\" name=\"a%s\" value=\"1\">" % i
    print "<hr>"

print "<input type=submit>"
print "</form>"
print "</body>"
print "</html>"
