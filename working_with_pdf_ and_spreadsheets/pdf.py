import PyPDF2     
f=open('ex.pdf','rb')
read=PyPDF2.PdfFileReader(f)
g=read.getPage(0)
h=g.extractText()
print(h)    