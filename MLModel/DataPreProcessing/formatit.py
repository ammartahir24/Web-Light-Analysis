import json
import os
data = json.load(open(os.path.normpath(os.getcwd() + os.sep  + 'dataset.json')))

print(len(data))

file = open('dataset.txt','a')
for k,v in data.items():
	line = ''
	main = k[1:-1]
	main = main.replace("u'","").replace("',","").replace("'","").split(" ")
	for each in main:
		line+=each
		line+=' '
	line+='\t'
	mini = v[1:-1]
	mini = mini.replace("u'","").replace("',","").replace("'","").split(" ")
	for i in mini:
		line+=i
		line+=' '
	line+='\n'
	file.write(line)

file.close() 