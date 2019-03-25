from html.parser import HTMLParser
from html.entities import name2codepoint
import os
import codecs
import csv

ind = 0
type_ = -1

class htmlspec:
    def __init__(self):
        self.parser = MyHTMLParser()
        self.script_count = 0
        self.img_count = 0
        self.div_count = 0
        self.hyp_count = 0
    def scriptplus(self):
        self.script_count+=1
    def imgplus(self):
        self.img_count+=1
    def divplus(self):
        self.div_count+=1
    def hypplus(self):
        self.hyp_count+=1
    def feed(self,content):
        self.parser.feed(content)



class pagespec:
    def __init__(self,type__):
        self.type = type__
        self.mobile_main = htmlspec()
        self.mobile_mini = htmlspec()
        self.web_main = htmlspec()
        self.web_mini = htmlspec()
    def handle(self, web):
        global type_,ind
        file = codecs.open(web+"/mobile/mini/index.html","rb")
        type_ = 0
        content = file.read()
        content = str(content)
        self.mobile_mini.feed(content)
        file = codecs.open(web+"/mobile/main/index.html","rb")
        type_ = 1
        content = file.read()
        content = str(content)
        self.mobile_main.feed(content)
        file = codecs.open(web+"/web/mini/index.html","rb")
        type_ = 2
        content = file.read()
        content = str(content)
        self.web_mini.feed(content)
        file = codecs.open(web+"/web/main/index.html","rb")
        type_ = 3
        content = file.read()
        content = str(content)
        self.web_main.feed(content)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global script_count,img_count,div_count,hyp_count,pages,ind,type_
        if tag=='img':
            if type_==0:
                pages[ind].mobile_mini.imgplus()
            if type_==1:
                pages[ind].mobile_main.imgplus()
            if type_==2:
                pages[ind].web_mini.imgplus()
            if type_==3:
                pages[ind].web_main.imgplus()
        elif tag=='script':
            if type_==0:
                pages[ind].mobile_mini.scriptplus()
            if type_==1:
                pages[ind].mobile_main.scriptplus()
            if type_==2:
                pages[ind].web_mini.scriptplus()
            if type_==3:
                pages[ind].web_main.scriptplus()
        elif tag=='div':
            if type_==0:
                pages[ind].mobile_mini.divplus()
            if type_==1:
                pages[ind].mobile_main.divplus()
            if type_==2:
                pages[ind].web_mini.divplus()
            if type_==3:
                pages[ind].web_main.divplus()
        elif tag=='a':
            if type_==0:
                pages[ind].mobile_mini.hypplus()
            if type_==1:
                pages[ind].mobile_main.hypplus()
            if type_==2:
                pages[ind].web_mini.hypplus()
            if type_==3:
                pages[ind].web_main.hypplus()
    # def handle_endtag(self, tag):

    # def handle_data(self, data):
    #     print("Data     :", data)

    # def handle_comment(self, data):
    #     print("Comment  :", data)

    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)

    # def handle_decl(self, data):
    #     print("Decl     :", data)




count = 0
ncount = 0

pages = []
parser = MyHTMLParser()
with open('top-1m.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for web in csv_reader:
        if count>=999:
            break
        if os.path.exists(web[1]):
            newpage = pagespec(1)
            pages.append(newpage)
            newpage.handle(web[1])
            count+=1
            ind+=1
        elif os.path.exists("non_transcoded/"+web[1]):
            newpage = pagespec(0)
            pages.append(newpage)
            newpage.handle("non_transcoded/"+web[1])
            ncount+=1
            ind+=1
        print("Parsed: ", count, ncount)


with open('dataset.csv', mode='w') as ds:
    dswriter = csv.writer(ds, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dswriter.writerow(['Main Mobile Script tags','Main Mobile Image tags','Main Mobile Div tags','Main Mobile Hyperlink tags','Mini Mobile Script tags','Mini Mobile Image tags','Mini Mobile Div tags','Mini Mobile Hyperlink tags','Main Web Script tags','Main Web Image tags','Main Web Div tags','Main Web Hyperlink tags','Mini Web Script tags','Mini Web Image tags','Mini Web Div tags','Mini Web Hyperlink tags','Transcoded'])
    for i in pages:
        dswriter.writerow([i.mobile_main.script_count,i.mobile_main.img_count,i.mobile_main.div_count,i.mobile_main.hyp_count,i.mobile_mini.script_count,i.mobile_mini.img_count,i.mobile_mini.div_count,i.mobile_mini.hyp_count,i.web_main.script_count,i.web_main.img_count,i.web_main.div_count,i.web_main.hyp_count,i.web_mini.script_count,i.web_mini.img_count,i.web_mini.div_count,i.web_mini.hyp_count,i.type])


