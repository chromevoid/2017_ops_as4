#!/usr/bin/python

import cgi
import cgitb
import os
import random

cgitb.enable()
form = cgi.FieldStorage


def present_quiz():
    routes = "1,2,3,4,5,6,7,A,C,E,B,D,F,M,G,J,Z,L,N,Q,W,R,S".split(",")

    lines = open('/home/unixtool/data/mta/StationEntrances.csv').read().splitlines()
    # lines = open('StationEntrances.csv').read().splitlines()
    lines.pop(0)
    random.shuffle(lines)
    c = 0.0011
    questions = []
    station_names = []
    options = []
    answers = []
    station_positions = []
    map_ranges = []
    for i in range(0, 5):
        questions.append(lines.pop(0).split(','))  # get the question line
        station_names.append(questions[i][2])  # get the name of the station
        station_positions.append([questions[i][3], questions[i][4]])  # get the map position of the station
        map_ranges.append([float(questions[i][4]) - c, float(questions[i][3]) - c,
                           float(questions[i][4]) + c, float(questions[i][3]) + c])  # get the map range
        valid_routes = []  # get the routes that stop at this station
        for j in range(0, 11):
            if questions[i][5 + j] != '':
                valid_routes.append(questions[i][5 + j])
        invalid_routes = [r for r in routes if r not in valid_routes]  # get the routes that don't stop at this station
        random.shuffle(valid_routes)  # shuffle the list
        random.shuffle(invalid_routes)  # shuffle the list
        options.append([])
        options[i].append(valid_routes.pop(0))  # get one correct answer
        answers.append(options[i][0])
        for j in range(0, 3):  # get three incorrect answer
            options[i].append(invalid_routes.pop(0))
        random.shuffle(options[i])  # shuffle the list

    print "Content-type: text/html"
    print
    print "<html>"
    print "<head>"
    print "<title>MTA Subway Quiz</title>"
    print "</head>"
    print "<body>"

    print "<h1>MTA Subway Quiz</h1>"
    print "<form method=GET action=\"MTAquiz.cgi\">"

    for i in range(0, 5):
        print "<p>Question " + str(i+1) + ": Which line stops at <strong>" + station_names[i] + "</strong>?</p>"
        print "<p><iframe width=\"425\" height=\"350\" frameborder=\"0\" scrolling=\"no\" marginheight=\"0\" " +\
              "marginwidth=\"0\" src=\"http://www.openstreetmap.org/export/embed.html?bbox=" +\
              str(map_ranges[i][0]) + "," + str(map_ranges[i][1]) + "," + str(map_ranges[i][2]) + "," + str(map_ranges[i][3]) +\
              "&amp;layer=hot&amp;marker=" + station_positions[i][0] + "," + station_positions[i][1] + \
              "\" style=\"border: 1px solid black\"></iframe></p>"
        print "<input type=\"radio\" name=\"q" + str(i+1) + "\" value=\"" + options[i][0] + "\">" + options[i][0] + "<br>"
        print "<input type=\"radio\" name=\"q" + str(i+1) + "\" value=\"" + options[i][1] + "\">" + options[i][1] + "<br>"
        print "<input type=\"radio\" name=\"q" + str(i+1) + "\" value=\"" + options[i][2] + "\">" + options[i][2] + "<br>"
        print "<input type=\"radio\" name=\"q" + str(i+1) + "\" value=\"" + options[i][3] + "\">" + options[i][3] + "<br>"
        print "<input type=\"hidden\" name=\"s" + str(i+1) + "\" value=\"" + station_names[i] + "\">"
        print "<input type=\"hidden\" name=\"a" + str(i+1) + "\" value=\"" + answers[i] + "\">"
        print "<hr>"

    print "<input type=submit value=\"submit\" name=\"submit\">"
    print "</form>"
    print "</body>"
    print "</html>"


def grade_answer():
    # stations = [form['s1'].value]
    # correct_answers = [form['a1'].value]
    # user_answers = [form['q1'].value]
    stations = ["1", "2"]
    correct_answers = ["A", "B"]
    user_answers = ["A", "A"]
    grade = 0
    correct = []
    incorrect = []
    for i in range(0, len(correct_answers)):
        if correct_answers[i] == user_answers[i]:
            grade += 1
            correct.append(stations[i])
        else:
            incorrect.append(stations[i])
    grade = grade * 100 / len(correct_answers)
    print "Content-type: text/html"
    print
    print "<html>"
    print "<head>"
    print "<title>MTA Subway Quiz Grading</title>"
    print "</head>"
    print "<body>"
    print "<h2>Your Score: " + str(grade) + "%</h2>"
    print "<h3>Correct answers</h3>"
    for element in correct:
        print "<p style=\"color: green\">" + str(element) + "</p>"
    print "<h3>Incorrect answers</h3>"
    for element in incorrect:
        print "<p style=\"color: red\">" + str(element) + "</p>"
    print "</body>"
    print "</html>"


query = os.environ["QUERY_STRING"]
if query:
    grade_answer()
else:
    present_quiz()
