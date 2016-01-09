import PyPDF2

def rotatePage(filename, filenameOut = "out.pdf", degree = 180):
    if filename.endwith(".pdf"):
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
