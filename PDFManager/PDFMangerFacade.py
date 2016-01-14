from pdfrw import PdfReader, PdfWriter,PageMerge
import PyPDF2
import os

class PDFMangerFacade:

    def encrypt(file_name, password, filenameOut="cripted.pdf"):

        if(not  (isinstance(file_name,str) and isinstance(filenameOut,str)) ):
            raise Exception('Errore: I nomi dei file devono essere stringhe')

        if(filenameOut.endswith('.pdf') == False):
            filenameOut = filenameOut + ".pdf"

        if(isinstance(password,str)):
             raise Exception('Errore: La password deve essere una stringa')

        if(file_name.endswith(".pdf") ):
            pdf_in = open(file_name, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_in)
            pdf_writer = PyPDF2.PdfFileWriter()

            for pagenum in range(pdf_reader.numPages):
                page = pdf_reader.getPage(pagenum)
                pdf_writer.addPage(page)


            pdf_writer.encrypt(password)
            pdf_out = open(filenameOut, 'wb')
            pdf_writer.write(pdf_out)
            pdf_out.close()
            pdf_in.close()
        else:
            raise Exception('Errore: Il nome del file deve terminare con .pdf')

    def watermark(file_name, file_watermark, filenameOut="newfile.pdf"):

        if(not  (isinstance(file_name,str) and isinstance(file_watermark,str) and isinstance(filenameOut,str)) ):
            raise Exception('Errore: I nomi dei file devono essere stringhe')

        if(filenameOut.endswith('.pdf') == False):
            filenameOut = filenameOut + '.pdf'

        if(file_name.endswith(".pdf") and file_watermark.endswith(".pdf")):
            ipdf = PdfReader(file_name)
            wpdf = PdfReader(file_watermark)

            wmark = PageMerge().add(wpdf.pages[0])[0]

            for page in ipdf.pages:
                PageMerge(page).add(wmark).render()

            PdfWriter().write(filenameOut, ipdf)
        else:
            raise Exception("Errore: Il primo e il secondo parametro devono terminare con .pdf")

    def merge(*varargs, filenameOut='merge_file'):
        if (len(varargs) <=1):
            raise Exception('Errore: utilizzare almeno due file.')

        if(not  (isinstance(filenameOut,str)) ):
            raise Exception('Errore: filenameOut deve essere una stringa.')

        if(filenameOut.endswith('.pdf') == False):
            filenameOut = filenameOut + ".pdf"

        writer = PdfWriter()

        for fname in varargs:
            if(isinstance(fname,str) == False):
                raise ValueError("Errore: Tutti i parametri devono essere stringhe.")
            if not fname.endswith('.pdf'):
                raise Exception("Errore: tutti i parametri devono terminare con .pdf")

            reader = PdfReader(fname)
            writer.addpages(reader.pages)

        writer.write(filenameOut)

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

        if (not (isinstance(filenameOut,  str) and isinstance(filename,str))):
            raise Exception("Errore: il nome dei file deve essere di tipo str ")

        if(filenameOut.endswith('.pdf') == False):
            filenameOut = filenameOut+'.pdf'

        if (filename.endswith(".pdf")):

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
            raise Exception("Errore: il file deve essere un pdf")

    def stitching(filename, filenameOut='out'):
        if( not( isinstance(filename,str) and isinstance(filenameOut,str)) ):
            raise Exception('Errore: I nomi dei file devono essere stringhe')

        if(not filenameOut.endswith('.pdf')):
            filenameOut = filenameOut+'.pdf'

        if filename.endswith(".pdf"):
            infile = PdfReader(filename)
        else:
            raise Exception("Errore: il file deve essere un pdf")
        for i, p in enumerate(infile.pages):
            PdfWriter().addpage(p).write(filenameOut + '_page-%02d.pdf' % (i + 1))

    def pagescount(filename):

        if( not isinstance(filename,str)):
            raise Exception('Errore: filename deve essere una stringa')

        if(filename.endswith('.pdf') == False):
            raise Exception("Errore il nome del file deve terminare con .pdf")
        reader = PdfReader(filename)
        i = 0
        for x in reader.pages:
            i = i+1
        return i