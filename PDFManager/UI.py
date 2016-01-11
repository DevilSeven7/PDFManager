from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PDFManager.PDFMangerFacade import PDFMangerFacade

class PDFManager_UI:

    def __init__(self):
        self.files=[]
        self.root = Tk()
        self.root.title('PDFManager')

        self.frame = Frame(self.root,height=2,bd=2,relief=SUNKEN,bg='black',)

        self.button_merge = Button(self.root,text = 'Unisci')
        self.button_split = Button(self.root,text = 'Dividi')
        self.button_stitching = Button(self.root,text = 'Fusione')
        self.button_watermark = Button(self.root,text = 'Filigrana')
        self.button_encript = Button(self.root,text = 'Cripta')
        self.button_rotate = Button(self.root,text='Ruota')

        self.password = Entry(self.root)
        self.combo_rotate = ttk.Combobox(self.root,state='readonly')
        self.combo_rotate['values'] = (0,90,180,270)
        lblPass = Label(self.root,text='Password :',anchor=E)
        lblGradi = Label(self.root,text='Gradi ;',anchor=E)

        self.button_add = Button(self.root,text='Aggiungi PDF',command=self.aggiungi)
        self.button_delete = Button(self.root,text='Rimuovi selezionato',command=self.rimuovi)

        self.list_file = ttk.Treeview(self.root)
        self.list_file['columns'] =('NumeroPagine')

        self.list_file.heading("#0",text='NomeFile')
        self.list_file.column('#0',anchor=W)
        self.list_file.heading('NumeroPagine',text = 'Numero pagine')
        self.list_file.column('NumeroPagine',anchor='center',width=100)


        self.button_add.grid(row=0, column= 0,columnspan=2,sticky=(W,E))
        self.button_delete.grid(row=1,column=0,columnspan=2,sticky=(W,E))
        self.list_file.grid(row=0,column=2,columnspan=3,rowspan=3)

        self.frame.grid(row=3,column=0,columnspan=5,sticky=(W,E),pady=5)

        self.button_merge.grid(row=4,column=0,columnspan=2,sticky=(W,E))
        self.button_stitching.grid(row=4,column=3,columnspan=2,sticky=(W,E))
        self.button_split.grid(row=5,column=0,columnspan=2,sticky=(W,E))
        self.button_watermark.grid(row=5,column=3,columnspan=2,sticky=(W,E))
        self.button_encript.grid(row=6,column=0,columnspan=2,sticky=(W,E))
        lblPass.grid(row=6,column=2)
        self.password.grid(row=6,column=3,columnspan=2,sticky=(W,E))

        self.button_rotate.grid(row=7,column=0,columnspan=2,sticky=(W,E))
        lblGradi.grid(row=7,column=2)
        self.combo_rotate.grid(row=7,column=3,columnspan=2,sticky=(W,E))

    def aggiungi(self):
        i = 0
        filelist = filedialog.askopenfilenames(filetypes=[("PDF file",".pdf")])
        for file in filelist:
            self.files.append(file)
            split = file.split("/").pop()
            self.list_file.insert("",i,text=split,values=(PDFMangerFacade.pagescount(file)))
            i = i+1

    def rimuovi(self):
        try:
            pos = self.list_file.selection()[0]
            posizione = self.list_file.index(pos)
            del(self.files[posizione]);
            self.list_file.delete(pos)
            for x in self.files:
                print(x)
        except IndexError:
            messagebox.showwarning("Warning","Nessun elemento selezionato")

    def start(self):
        self.root.mainloop()