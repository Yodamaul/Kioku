def details(name):
	anna = {'name': 'Anna', 'age': '22', 'relation': 'Daughter'}
	yasutaka = {'name': 'Yasutaka', 'age': '21', 'relation': 'son'}
	pushkar = {'name': 'Pushkar', 'age': '24', 'relation': 'son'}
	kush = {'name': 'Kush', 'age': '18', 'relation': 'friend'}
	meow = {'name': 'Meow-Ludo Disco Gamma Meow-Meow', 'age': '24', 'relation':'Stranger'}


	if(name == 'Anna Choi'):
		return('Name: '+ str(anna['name']) + ' Age: ' + str(anna['age']) + ' Relation: ' + str(anna['relation']))
	elif(name == 'Pushkar Kadam'):
		return('Name: '+ str(pushkar['name']) + ' Age: ' + str(pushkar['age']) + ' Relation: ' + str(pushkar['relation']))
	elif(name == 'Yasutaka'):
		return('Name: '+ str(yasutaka['name']) + ' Age: ' + str(yasutaka['age']) + ' Relation: ' + str(yasutaka['relation']))
	elif(name == 'Kush'):
		return('Name: '+ str(kush['name']) + ' Age: ' + str(kush['age']) + ' Relation: ' + str(kush['relation']))
	elif(name == 'Meow'):
		return('Name: '+ str(meow['name']) + ' Age: ' + str(meow['age']) + ' Relation: ' + str(meow['relation']))
	else:
		return('Unknown')