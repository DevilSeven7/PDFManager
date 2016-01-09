'''
Created on 28/dic/2015

@author: pippo
'''
from pdfrw import PdfReader, PdfWriter, PageMerge 

even = PdfReader('pdf_file/esami.pdf') 
odd = PdfReader('pdf_file/newfile.pdf') 
all = PdfWriter() 
blank = PageMerge() 
blank.mbox = [0, 0, 612, 792] # 8.5 x 11 
blank = blank.render() 
all.addpage(blank)

for x,y in zip(odd.pages, even.pages):
    all.addpage(x) 
    all.addpage(y) 
while len(all.pagearray) % 2:
    all.addpage(blank)

all.write('all.pdf')