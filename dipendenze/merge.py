import os

from pdfrw import PdfReader, PdfWriter

def merge(*varargs,merge_file):

    if(merge_file.endswith('.pdf')):
        merge_file = merge_file+".pdf"

    for x in varargs:
        if(isinstance(x,str) == False):
            raise Exception("Errore: Tutti i parametri devono essere stringhe.")

    writer = PdfWriter()
    files = []
    for x in varargs :
        if x.endswith('.pdf'):
            files.add(x)
        else:
            raise Exception("Errore tutti i parametri devono terminare con .pdf")
    for fname in sorted(files):
        writer.addpages(PdfReader(os.path.join('pdf_file', fname)).pages)

    writer.write("output.pdf")
