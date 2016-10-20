import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"
#created = True# gives an error if you try to make the same table twice
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops



#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

#q = "CREATE TABLE students (name TEXT, id INTEGER)"
#c.execute(q)    #run SQL query


fObj = open("peeps.csv") 
d=csv.DictReader(fObj)
##q = "CREATE TABLE students (name TEXT, id INTEGER)"
##c.execute(q)    #run SQL query
for a in d:
	command = "INSERT INTO students VALUES('" + a['name'] +"'," + a['id']+ ")"
	c.execute(command)

	

sObj = open("courses.csv")
x = csv.DictReader(sObj)
#p = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
#c.execute(p)
for b in x:
	command = "INSERT INTO courses VALUES('"+ b['code'] + "'," + b['mark']+"," + b['id']+")"
	c.execute(command)


	    #run SQL query
	

#p = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
#c.execute(p)


#==========================================================

db.commit() #save changes
db.close()  #close database
