from html.parser import HTMLParser
from html.entities import name2codepoint
import os
import codecs
import csv


minitags = {}
maintags = {}
mini = True
starttags = []
endtags = []

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global mini,minitags,maintags,starttags
		starttags.append(tag)
		if mini==True:
			if tag not in minitags:
				minitags[tag] = 1
			else:
				minitags[tag]+=1
		else:
			if tag not in maintags:
				maintags[tag] = 1
			else:
				maintags[tag]+=1
	def handle_endtag(self,tag):
		global endtags
		endtags.append(tag)

count = 0
with open('top-1m.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for web in csv_reader:
        print web
        web = web[1]
        if count>=1284:
            break
        if os.path.exists(web):
	        file = codecs.open(web+"/mobile/mini/index.html","rb")
	        file2 = codecs.open(web+"/mobile/main/index.html","rb")
	        content = file.read()
	        content = str(content)
	        content2 = file2.read()
	        content2 = str(content2)
	        parser = MyHTMLParser()
	        parser2 = MyHTMLParser()
	        try:
	        	mini = True
	        	parser.feed(content)
	        	mini = False
	        	parser2.feed(content2)
	        except Exception as e:
	        	print (e)
	        else:
	        	pass
	        finally:
	        	pass
	        count+=1


minitag = sorted(minitags.items(), key=lambda kv: kv[1])
maintag = sorted(maintags.items(), key=lambda kv: kv[1])

for k,v in minitag:
	if v>10:
		print k,': ',v
print("MAIN TAGS")
for k,v in maintag:
	if v>10:
		print k,': ',v


selfclosetags = []
setofstarttags = set(starttags)
setofendtags = set(endtags)
for tag in setofstarttags:
	if tag not in setofendtags and (starttags.count(tag)>10 or endtags.count(tag)>10):
		selfclosetags.append(tag)

print(selfclosetags)
print (len(selfclosetags),len(starttags),len(endtags))