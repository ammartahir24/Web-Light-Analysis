import os
import sys
import re
import codecs
import shutil
import csv

fail = "<b>Transcoding test failed:</b><br>This page could not be transcoded due to technical issues.</div>"
count = 0
convert_count = 0
downspeed = ' 2>&1 | grep -o "[0-9.]\+ [KM]*B/s"'
wget = "wget --connect-timeout=10 "
index = "index.html "
fname = "--output-document="
htheaderm = '--user-agent="Mozilla/5.0 (Linux; U; Android 2.3.6; en-gb; GT-S6102 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1" ' #copy phone's header
htheaderw = '--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" ' #copy web's header
weblite = "http://googleweblight.in/?lite_url=http://"

def scrap(web):
	global count
	global convert_count
	if os.path.exists(web):
		count+=1
		convert_count+=1
		return
	if os.path.exists(nt+"/"+web):
		count+=1
		return
	os.system("clear")
	print convert_count,"out of",count,"websites converted successfully.\n"
	os.makedirs(web+"/mobile/main")
	cl = wget+fname+web+"/mobile/main/"+index+htheaderm+web+downspeed
	os.makedirs(web+"/mobile/mini")
	cl2 = wget+fname+web+"/mobile/mini/"+index+htheaderm+weblite+web+downspeed
	os.system(cl2)
	file = codecs.open(web+"/mobile/mini/index.html","rb")
	content = file.read()
	content = str(content)
	if re.search(fail,content):
		shutil.rmtree(web)
		os.system("clear")
		os.makedirs(nt+"/"+web+"/mobile/main")
		cl = wget+fname+nt+"/"+web+"/mobile/main/"+index+htheaderm+web+downspeed
		os.makedirs(nt+"/"+web+"/mobile/mini")
		cl2 = wget+fname+nt+"/"+web+"/mobile/mini/"+index+htheaderm+weblite+web+downspeed
		os.system(cl2)
		os.system(cl)
		os.makedirs(nt+"/"+web+"/web/main")
		cl = wget+fname+nt+"/"+web+"/web/main/"+index+htheaderw+web+downspeed
		os.makedirs(nt+"/"+web+"/web/mini")
		cl2 = wget+fname+nt+"/"+web+"/web/mini/"+index+htheaderw+weblite+web+downspeed
		os.system(cl)
		os.system(cl2)
		os.system("clear")
	
	else:
		os.system(cl)
		os.makedirs(web+"/web/main")
		cl = wget+fname+web+"/web/main/"+index+htheaderw+web+downspeed
		os.makedirs(web+"/web/mini")
		cl2 = wget+fname+web+"/web/mini/"+index+htheaderw+weblite+web+downspeed
		os.system(cl)
		os.system(cl2)
		os.system("clear")
		convert_count+=1
	count+=1

nt = "non_transcoded"
if not os.path.exists(nt):
	os.makedirs(nt)

with open('top-1m.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')
	for web in csv_reader:
		if convert_count==1000:
			break
		scrap(web[1])


	
# webs = [
# "facebook.com", "express.pk", "geo.tv", "twitter.com","youtube.com"]

# for web in webs:
# 	scrap(web)


