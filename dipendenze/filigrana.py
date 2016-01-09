'''
Created on 28/dic/2015

@author: pippo
'''
from pdfrw import PdfReader, PdfWriter,PageMerge
def watermark(file_name,file_watermark,a = 'newfile.pdf'):
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