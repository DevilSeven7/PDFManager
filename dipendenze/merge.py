import os

from pdfrw import PdfReader, PdfWriter

writer = PdfWriter()

files = [x for x in os.listdir('pdf_file')if x.endswith('.pdf')] 

for fname in sorted(files): 
    writer.addpages(PdfReader(os.path.join('pdf_file', fname)).pages)

writer.write("output.pdf")
