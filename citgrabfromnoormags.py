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
    urlretrieve(cit, dst)
    tempFile=open(dst, 'r+')
    tempFile.write( dst.replace( a, "@Article{" ) )
    tempFile.close()



