import sqlite3   #enable control of an sqlite database



f = "discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
og = db.cursor() #da real og


def getGrades():
	command = "SELECT name, students.id, code, mark FROM students, courses WHERE students.id = courses.id"
	og.execute(command)
	finStr = ""
	for item in og:
		print item
		finStr += item[0]
		finStr += item[1]
	return finStr	


print(getGrades())



# #==========================================================

db.commit() #save changes
db.close()  #close database