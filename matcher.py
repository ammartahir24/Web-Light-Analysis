import os
import json
from fuzzywuzzy import fuzz



dict_main = json.load(open(os.path.normpath(os.getcwd() + os.sep  + '\\parsed_main.json')))
dict_mini= json.load(open(os.path.normpath(os.getcwd() + os.sep +   '\\parsed_mini.json')))

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
		# Partial_Ratio = fuzz.partial_ratio(x.lower(),y.lower())
		Token_Sort_Ratio = fuzz.token_sort_ratio(x,y)
		# Token_Set_Ratio = fuzz.token_set_ratio(x,y)
		# print(Ratio)
		# print(Partial_Ratio)
		# print(Token_Sort_Ratio)
		# print(Token_Set_Ratio)
		if(Ratio > 80 and Token_Sort_Ratio> 85):
			print("Both match >90")
			print(Ratio)
			print(Token_Sort_Ratio)
			print(x)
			print(y)
			print()
		elif(Token_Sort_Ratio > 85):
			print("token match only >90")
			print(Token_Sort_Ratio)
			print(x)
			print(y)
			print()
		elif(Ratio > 85):
			print("ratio match only >90")
			print(Ratio)
			print(x)
			print(y)
			print()

		# if(Token_Set_Ratio > 90):
		# 	print("more than 80 percent Match")
		# 	print(Token_Set_Ratio)
		# 	# print(x)
		# 	# print(y)
		# 	print()	
				
