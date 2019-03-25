# Web-Light-Analysis

Learn Google’s Web Light Transformations via Deep Learning (CNN)
- Ammar Tahir
- Adil Inam

Introduction:
Improving user experience on internet has always been a primary motivation for many improved internet protocols and architectures. Today when there are more than 3.6 billion unique users on internet and a big part of them are from developing nations, it is extremely critical that users from developing countries do not face lags because of limited resources. To address this problem, Google launched Google Web Light which facilitates loading pages faster on slower internet connections by performing multiple transformations and compressions on the html pages. Aim of this project is to perform detailed analysis of transformed pages from Web Light and try to learn using Machine Learning, what optimizations and transformations are being performed. Learning these transformations can help us further in reducing complexities associated with slower connections and low-end devices and improving user experience further.

Sor far, we have collected our dataset, run preliminary analysis and we are in initial stages of setting up a neural network to study web light transformations.
> Scrapper.py collects top 1000 alexa pages in 4 forms:  
* Low end mobile browser page
* Low end mobile browser page transformed through weblight
* Desktop version of web page
* Desktop version of web page transformed through weblight
This dataset can be found here : https://drive.google.com/file/d/1h3EtF80XXlc68HjE2s-swSnK1FbnqmNG/view?usp=sharing
> Parse.py parses these pages and extracts out metadata like counts of different tags, for this preliminary analysis we are looking at four particular tags:
* div tag
* img tag
* script tag
* hyperlink (a) tag
> dataset.csv consists of the data produced by parse.py. It consists of 17 columns corresponding to each web site, 16 being counts of forementioned tags and 1 being a binary variable for whether website was transcodable by weblight or not. (Weblight does not transcode a few web sites, In our data set of 1181, 182 websites were not transcodable.)
> Analysis.ipynb shows analysis of dataset collected above. It gives visualisation of trend followed in transformations of web pages by web light.
