import dipendenze
import re
import string

class PDFMangerFacade:

    def __init__(self):
        None

    def merge(*varargs,a = 'merge_file'):
        for x in varargs:
            if (PDFMangerFacade.__is_safe__(x) == False):
                raise Exception("Errore: Non utilizzare path assolute o relative")

        dipendenze.merge(varargs,a)

    def watermark(file_name,file_watermark,a = 'newfile.pdf'):
        if( (PDFMangerFacade.__is_safe__(file_name) == False) and (PDFMangerFacade.__is_safe__(file_watermark) == False) and (PDFMangerFacade.__is_safe__(a) == False)):
            raise Exception("Errore: Non utilizzare path assolute o relative")
        dipendenze.watermark(file_name,file_watermark,a)

    def encrypt(file_name,password,a = 'rotated.pdf'):
        if( (PDFMangerFacade.__is_safe__(file_name) == False) and (PDFMangerFacade.__is_safe__(a) == False)):
            raise Exception("Errore: Non utilizzare path assolute o relative")

        dipendenze.encrypt(file_name,a)

    def stitching(filename):
        if(PDFMangerFacade.__is_safe__(filename) == False):
            raise Exception("Errore: Non utilizzare path assolute o relative")
        dipendenze.stitching(filename)

    def rotatePage(filename, filenameOut = "out.pdf", degree = 180):
        if(PDFMangerFacade.__is_safe__(filename)):
             raise Exception("Errore: Non utilizzare path assolute o relative")
        dipendenze.rotatePage(filename, filenameOut, degree)

    def __is_safe__(filename):
        return not (filename.startswith(("/", "\\")) or             #path assoluta
                    (len(filename) > 1 and filename[1] == ":" and   #D:
                     filename[0] in string.ascii_letter) or
                    re.search(r"[.] [.] [/\\]", filename))          #path relativa