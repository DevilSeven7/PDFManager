import PyPDF2

def encrypt(file_name,password,a = 'rotated.pdf'):
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