from html.parser import HTMLParser
import os
import codecs
import csv
import copy
from html.entities import name2codepoint


stack = []
datadict = {}

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag :", tag)
        stack.append(tag)

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        j = len(stack)
        while(j>0 and stack[j-1]!=tag):
        	del stack[-1]
        	j = len(stack)
        if j>0:
	        del stack[-1]

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        datadict[data] = copy.deepcopy(stack)

parser = MyHTMLParser()
parser.feed('<html><head><title><img src="none.png">Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

# print datadict

def stringed(ddict):
	ret = ''
	for k,v in ddict.iteritems():
		ret+=(k+str(v)+'\n')
	return ret



count = 0
with open('top-1m.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for web in csv_reader:
        web = web[1]
        if count>=1284:
            break
        if os.path.exists(web):
        	datadict = {}
	        file = codecs.open(web+"/mobile/mini/index.html","rb")
	        file2 = codecs.open(web+"/mobile/main/index.html","rb")
	        content = file.read()
	        content = str(content)
	        parser = MyHTMLParser()
	        try:
	        	parser.feed(content)
	        	data = stringed(datadict)
	        	f = open(web+"/mobile/mini/parsed.txt",'a')
	        	f.write(data)
	        	f.close()
	        	datadict = {}
        		print web
	        except Exception as e:
	        	print (e)
	        else:
	        	pass
	        finally:
	        	pass
	        content2 = file2.read()
	        content2 = str(content2)
	        parser2 = MyHTMLParser()
	        try:
	        	parser2.feed(content2)
	        	data = stringed(datadict)
	        	f = open(web+"/mobile/main/parsed.txt",'a')
	        	f.write(data)
	        	f.close()
	        	datadict ={}
	        except Exception as e:
	        	print (e)
	        else:
	        	pass
	        finally:
	        	pass
	        count+=1
