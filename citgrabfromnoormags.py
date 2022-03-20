import codecs
from urllib.request import urlretrieve
l=input("Number of Articles?  "
l=int(l)
url='index.html'
response = codecs.open(url, "r","utf-8")
html = response.read()
stop=1
for b in range(l):
    print  (b)
    start= html.index('href="https://www.noormags.ir/view/fa/articlepage/',stop)+50
    stop = html.index('/',start)
    a=html[start:stop]
    cit= "https://www.noormags.ir/view/fa/citation/bibtex/"+a
    dst = a+".bib"
    h="""@Article{"""
    urlretrieve(cit, dst)
    tempFile=open(dst, 'r')
    got=tempFile.read()
    got=got.replace(got[0:1],"")
    tempFile.close()
    tempFile=open(dst, 'w')
    tempFile.write(h+got)
    tempFile.close()


