import csv

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)



def peeplez():
	masterLis =[]
	for k in d:
		miniLis = [k['name'], k['age'], k['id']]
		masterLis.append(miniLis)
	return masterLis
		#print k['name'], k['age'], k['id']


def coursez():
	masterLis =[]
	for k in d:
		miniLis = [k['code'], k['mark'], k['id']]
		masterLis.append(miniLis)
	return masterLis	
	#print k['name'],",", k['id']
    #Q: What can you print here to make each line show only
    #   a name and its ID?
    #   eg,
    #   sasha, 3


