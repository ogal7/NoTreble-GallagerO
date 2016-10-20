import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"
#created = True# gives an error if you try to make the same table twice
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
og = db.cursor() #da real og



y = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
gaga = og.execute(y)
#print gaga
#print "haha"
for foo in gaga:
	print foo[0]




#==========================================================

db.commit() #save changes
db.close()  #close database
