'''
Created on 28/dic/2015

@author: pippo
'''
from pdfrw import PdfReader, PdfWriter

infile = PdfReader('bianco.pdf') 
for i, p in enumerate(infile.pages): 
    PdfWriter().addpage(p).write('page-%02d.pdf' % i) 