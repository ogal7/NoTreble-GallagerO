import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="grades.db"
#created = True# gives an error if you try to make the same table twice
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
og = db.cursor() #da real og
filled = True



#==========================================================


if (filled == False):
 	q = "CREATE TABLE students (name TEXT, id INTEGER)"
 	c.execute(q)    #run SQL query
 	p = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
 	c.execute(p)
 	fObj = open("peeps.csv") 
 	d=csv.DictReader(fObj)
 	for a in d:
 		command = "INSERT INTO students VALUES('" + a['name'] +"'," + a['id']+ ")"
 		c.execute(command)

 	sObj = open("courses.csv")
 	x = csv.DictReader(sObj)

 	for b in x:
 		command = "INSERT INTO courses VALUES('"+ b['code'] + "'," + b['mark']+"," + b['id']+")"
 		c.execute(command)
 	filled = True




#Using python and the database from the previous assignment write a program to do the following:

#	Look up the grades for each student.
#	Compute the average for each student.
#	Display each students name, id and average.

#The points above are not specific steps you need to take in a particular order. You should organize the code however you feel will accomplish the task best.




y = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id "
gaga = og.execute(y)
for f in gaga:
	print f[0]

#def computeAvg():

#def displayShit():








#==========================================================

db.commit() #save changes
db.close()  #close database
