from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PDFManager.PDFMangerFacade import PDFMangerFacade

class PDFManager_UI:

    def __init__(self):
        self.i= -1;
        self.files=[]
        self.root = Tk()
        self.root.title('PDFManager')

        self.frame = Frame(self.root,height=2,bd=2,relief=SUNKEN,bg='black',)

        self.button_merge = Button(self.root,text = 'Unisci',command=self.unisci)
        self.button_stitching = Button(self.root,text = 'Dividi',command=self.dividi)
        self.button_split = Button(self.root,text = 'Fusione',command=self.fusione)
        self.button_watermark = Button(self.root,text = 'Filigrana',command=self.filigrana)
        self.button_encript = Button(self.root,text = 'Cripta',command=self.cripta)
        self.button_rotate = Button(self.root,text='Ruota',command=self.ruota)
        self.button_clear =Button(self.root,text='Rimuovi tutto',command=self.svuota)

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
        self.button_clear.grid(row = 2,column=0,columnspan=2,sticky=(W,E))
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

        self.button_stitching.config(state=DISABLED)
        self.button_encript.config(state=DISABLED)
        self.button_watermark.config(state=DISABLED)
        self.button_merge.config(state=DISABLED)
        self.button_split.config(state=DISABLED)
        self.button_rotate.config(state=DISABLED)

    def aggiungi(self):
        filelist = filedialog.askopenfilenames(filetypes=[("PDF file",".pdf")])
        for file in filelist:
            if(file in self.files):
                continue
            self.i = self.i+1
            self.files.append(file)
            split = file.split("/").pop()
            self.list_file.insert("",self.i,text=split,values=(PDFMangerFacade.pagescount(file)))

        self.controlla()

    def rimuovi(self):
        try:
            pos = self.list_file.selection()[0]
            posizione = self.list_file.index(pos)
            del(self.files[posizione])
            self.list_file.delete(pos)
            self.i= self.i-1
            print(self.files)

        except IndexError:
            messagebox.showwarning("Attenzione","Nessun elemento selezionato")
        self.controlla()

    def unisci(self):
        try:
            name = filedialog.asksaveasfilename(filetypes=[("PDF file",".pdf")])
            if(name.endswith('.pdf') == False):
                name = name+'.pdf'
            PDFMangerFacade.merge(*self.files,a = name);
        except Exception as e:
            messagebox.showwarning("Attenzione",e)
    def svuota(self):
        self.files = []
        self.list_file.delete(*self.list_file.get_children())
    def dividi(self):
        try:
            pos = self.list_file.selection()[0]
            posizione = self.list_file.index(pos)
            phat = filedialog.askdirectory()
            prefisso = (self.files[posizione].split("/").pop()).split('.')[0]
            PDFMangerFacade.stitching(self.files[posizione],phat+'/'+prefisso)
        except IndexError:
            messagebox.showwarning("Attenzione","Elemento non selezionato")

    def fusione(self):

        try:
            name = filedialog.asksaveasfilename(filetypes=[("PDF file",".pdf")])
            PDFMangerFacade.splitting(*self.files,name)
        except IndexError as e:
            messagebox.showwarning("Attenzione",e)

    def filigrana(self):
        try:
            pos = self.list_file.selection()[0]
            posizione = self.list_file.index(pos)
            print(self.files[posizione])
            name_filigrana = filedialog.askopenfilename(filetypes=[("PDF file",".pdf")])
            name = filedialog.asksaveasfilename(filetypes=[("PDF file",".pdf")])
            PDFMangerFacade.watermark(self.files[posizione],name_filigrana,name)
        except IndexError:
            messagebox.showwarning("Attenzione","Elemento non selezionato.")


    def cripta(self):
        try:
            pos = self.list_file.selection()[0]
            posizione = self.list_file.index(pos)
            password = self.password.get()
            if(password == ""):
                messagebox.showwarning("Attenzione","Inserire una password.")
                return
            name = filedialog.asksaveasfilename(filetypes=[("PDF file",".pdf")])
            PDFMangerFacade.encrypt(self.files[posizione],password,name);
            self.password.delete(0,'end')
        except IndexError:
            messagebox.showwarning("Attenzione","Elemento non selezionato.")

    def ruota(self):
        try:
            pos = self.list_file.selection()[0]
            posizione = self.list_file.index(pos)
            gradi = int(self.combo_rotate.get())
            name = filedialog.asksaveasfilename(filetypes=[("PDF file",".pdf")])
            PDFMangerFacade.rotatePage(self.files[posizione],name,gradi);
        except IndexError:
            messagebox.showwarning("Attenzione","Elemento non selezionato.")
        except ValueError:
            messagebox.showwarning("Attenzione","Selezionare il grado di rotazione.")

    def start(self):
        self.root.mainloop()

    def controlla(self):
        i = len(self.files)
        if(i == 0):
            self.button_stitching.config(state=DISABLED)
            self.button_encript.config(state=DISABLED)
            self.button_watermark.config(state=DISABLED)
            self.button_merge.config(state=DISABLED)
            self.button_split.config(state=DISABLED)
            self.button_rotate.config(state=DISABLED)
        if(i ==1):
            self.button_stitching.config(state=NORMAL)
            self.button_encript.config(state=NORMAL)
            self.button_watermark.config(state=NORMAL)
            self.button_merge.config(state=DISABLED)
            self.button_split.config(state=DISABLED)
            self.button_rotate.config(state=NORMAL)
        if(i >1):
            self.button_stitching.config(state=NORMAL)
            self.button_encript.config(state=NORMAL)
            self.button_watermark.config(state=NORMAL)
            self.button_merge.config(state=NORMAL)
            self.button_split.config(state=NORMAL)
            self.button_rotate.config(state=NORMAL)