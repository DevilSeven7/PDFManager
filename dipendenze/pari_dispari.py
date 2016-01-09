
from pdfrw import PdfReader, PdfWriter

def splitting(filenameOut ="out",*varargs):

    for file in varargs:
        if False == (isinstance(file,str)):
            raise ValueError("Errore: i file devono essere pdf")

    if False == (isinstance(filenameOut,str)):
            raise ValueError("Errore: il nome del file deve essere di tipo str")


    all = PdfWriter()
    numpage=float("inf")

    for file in varargs:
        reader = PdfReader(file)
        i=0
        for page in reader.pages:
            i=i+1
        if (numpage > i):
             numpage=i

    for i in range(numpage):
        for filename in varargs:
            reader = PdfReader(filename)
            all.addPage(reader.getPage(i))


    all.write(filenameOut+".pdf")



