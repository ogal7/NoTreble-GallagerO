import sqlite3   #enable control of an sqlite database



f = "discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
og = db.cursor() #da real og


d = {}



def getGrades(idee):
 	command = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
 	retStr = ""
 	sum = 0
 	ct = 0.0
 	#print "a"
 	for item in og.execute(command):
 		#print "b"
 		if item[1] in d.keys():
 			d[item[1]] += " " + item[2]
 			#sum += float(item[2])	
 			#ct +=1
 		else:
 			d[item[1]] = " "+ item[2]# id, code, grade
 			#sum += float(item[2])
 			#ct +=1
 			
 	for k in d:
 		if (k == str(idee)):
 			retStr += k + "\t" + d[k] + "\n"
 	print retStr
 	return retStr
	


def makeAvgs(idee):
	x = getGrades(idee)
	L = x.split(' ')
	i = 1.0
	sum = 0.0
	while (i < len(L)):
		sum += L[i]
		i+=1
	return sum/i


getGrades(2)
makeAvgs(1)



# # #==========================================================

db.commit() #save changes
db.close()  #close database