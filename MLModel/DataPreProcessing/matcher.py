import os
import json
from fuzzywuzzy import fuzz
import codecs
import csv

dataset = {}

count = 0
with open('top-1m.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')
	for web in csv_reader:
		web = web[1]
		if count>=1284:
			break
		if os.path.exists(web):
			count += 1
			print(web,count, len(dataset))
			if os.path.exists(web+'/mobile/main/parsed.json') and os.path.exists(web+'/mobile/mini/parsed.json'):
				try:
					dict_main = json.load(open(os.path.normpath(os.getcwd() + os.sep  + web + '/mobile/main/parsed.json')))
					dict_mini= json.load(open(os.path.normpath(os.getcwd() + os.sep +  web + '/mobile/mini/parsed.json')))
					main_keys = []
					mini_keys = []

					for key,value in dict_main.items():
						if not (key == "" or key  == " " or key == "'" or key == "\\" or len(key) < 4 ):
							main_keys.append(key)

					for key,value in dict_mini.items():
						if not (key == "" or key  == " " or key == "'" or key == "\\" or len(key) < 4 ):
							mini_keys.append(key)	

					for x in main_keys:
						for y in mini_keys:
							Ratio = fuzz.ratio(x.lower(),y.lower())
							Token_Sort_Ratio = fuzz.token_sort_ratio(x,y)
							if(Ratio > 90 and Token_Sort_Ratio> 90):
								sentence = str(dict_main[x])
								target = str(dict_mini[y])
								dataset[sentence] = target
				except Exception as e:
					print(e)



f = open("dataset.json",'a')
json.dump(dataset, f)
f.close() 						
