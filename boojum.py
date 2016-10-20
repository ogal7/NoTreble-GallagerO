import sqlite3   #enable control of an sqlite database


f = "discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
og = db.cursor() #da real og
d = {}



command = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
haha = og.execute(command)
for item in haha:
 	if (item[0] in d.keys()):
 		d[item[0]].append(item[2])
 	else:
 		d[item[0]] = [item[2]]
for k in d:
	sum41 = 0
	count = 0
 	for i in d[k]:
 		sum41+= i
 		count +=1
 	print str(k) + ": " + str(float(sum41/count))



# # #==========================================================

db.commit() #save changes
db.close()  #close database