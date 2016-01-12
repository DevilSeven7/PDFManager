from pdfrw import PdfReader, PdfWriter,PageMerge
import PyPDF2
import os

class PDFMangerFacade:

    def __init__(self):
        None

    def encrypt(file_name,password,a = "cripted.pdf"):

        if(a.endswith('.pdf') == False):
            a = a+".pdf"

        if(file_name.endswith(".pdf") ):
            if(isinstance(a,str)):
                pdf_in = open(file_name, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_in)
                pdf_writer = PyPDF2.PdfFileWriter()

                for pagenum in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(pagenum)
                    pdf_writer.addPage(page)


                pdf_writer.encrypt(password)
                pdf_out = open(a, 'wb')
                pdf_writer.write(pdf_out)
                pdf_out.close()
                pdf_in.close()
            else:
                raise Exception('Errore: il terzo parametro deve essere una stringa.')
        else:
            raise Exception('Errore: Il nome del file deve terminare con .pdf')

    def watermark(file_name,file_watermark,a = "newfile.pdf"):

        if(a.endswith('.pdf') == False):
            a = a+'.pdf'

        if(file_name.endswith(".pdf") and file_watermark.endswith(".pdf")):
            if(isinstance(a,str)):
                ipdf = PdfReader(file_name)
                wpdf = PdfReader(file_watermark)

                wmark = PageMerge().add(wpdf.pages[0])[0]

                for page in ipdf.pages:
                    PageMerge(page).add(wmark).render()

                PdfWriter().write(a, ipdf)
            else:
                raise Exception('Errore: Il terzo parametro deve essere una stringa.')
        else:
            raise Exception("Errore: Il primo e il secondo parametro devono terminare con .pdf")

    def merge(*varargs,a = 'merge_file'):
        if (len(varargs) <=1):
            raise Exception('Errore: utilizzare almeno due file.')

        if(a.endswith('.pdf') == False):
            a = a+".pdf"

        for x in varargs:
            if(isinstance(x,str) == False):
                raise ValueError("Errore: Tutti i parametri devono essere stringhe.")

        writer = PdfWriter()
        files = []
        for x in varargs :
            if x.endswith('.pdf'):
                files.append(x)
            else:
                raise Exception("Errore: tutti i parametri devono terminare con .pdf")
        for fname in files:
            reader = PdfReader(fname)
            writer.addpages(reader.pages)

        writer.write(a)

    def splitting(*varargs,filenameOut ="out"):

        if(len(varargs)<=1):
            raise IndexError("Errore: inserire almeno due file.")

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
        if(filenameOut.endswith('.pdf') == False):
            filenameOut = filenameOut+'.pdf'

        all.write(filenameOut)

    def rotatePage(filename, filenameOut = "out", degree = 180):

        if(filenameOut.endswith('.pdf') == False):
            filenameOut = filenameOut+'.pdf'

        if (filename.endswith(".pdf")):
            if isinstance(filenameOut,  str):
                if isinstance(degree, int):
                    pdf_in = open(filename, 'rb')
                    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
                    pdf_writer = PyPDF2.PdfFileWriter()

                    for pagenum in range(pdf_reader.numPages):
                        page = pdf_reader.getPage(pagenum)
                        page.rotateClockwise(degree)
                        pdf_writer.addPage(page)


                    pdf_out = open(filenameOut, 'wb')
                    pdf_writer.write(pdf_out)
                    pdf_out.close()
                    pdf_in.close()
                else:
                    raise ValueError("Errore: il grado deve essere di tipo int")
            else:
                raise Exception("Errore: il nome del file di output deve essere di tipo str ")
        else:
            raise Exception("Errore: il file deve essere un pdf")

    def stitching(filename,fileout = 'out'):
        if filename.endswith(".pdf"):
            infile = PdfReader(filename)
        else:
            raise Exception("Errore: il file deve essere un pdf")
        for i, p in enumerate(infile.pages):
            PdfWriter().addpage(p).write(fileout+'_page-%02d.pdf' % (i+1))

    def pagescount(filename):
        if(filename.endswith('.pdf') == False):
            raise Exception("Errore il nome del file deve terminare con .pdf")
        reader = PdfReader(filename)
        i = 0
        for x in reader.pages:
            i = i+1
        return i