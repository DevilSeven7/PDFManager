'''
Created on 28/dic/2015

@author: pippo
'''
from pdfrw import PdfReader, PdfWriter,PageMerge

ipdf = PdfReader("esami.pdf")
wpdf = PdfReader("RAD.pdf")

wmark = PageMerge().add(wpdf.pages[0])[0]

for page in ipdf.pages:
    PageMerge(page).add(wmark).render()

PdfWriter().write('newfile.pdf', ipdf)