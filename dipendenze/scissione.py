'''
Created on 28/dic/2015

@author: pippo
'''
from pdfrw import PdfReader, PdfWriter

def stitching(filename):
     if filename.endwith(".pdf"):
        infile = PdfReader(filename)
        for i, p in enumerate(infile.pages):
            PdfWriter().addpage(p).write('page-%02d.pdf' % i)

     else:
        raise Exception("Errore: il file deve essere un pdf")
