import os
from tkinter import StringVar, N, E, W, S, END, WORD, INSERT
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext 

class Convert(object):
    
    def __init__(self, master, path):
        self.nodes = dict()
        
        #containers
        self.content = ttk.Frame(master)
        self.frame = ttk.Frame(self.content)
        self.frameLeft = ttk.Frame(self.content)
        self.frameRight = ttk.Frame(self.content)

        #right
        self.contentRight = ttk.Frame(self.frameRight, padding=(3,3,3,3))
        #self.console = ttk.Entry(self.contentRight, justify='left')
        #self.console.grid(padx=0,pady=0,ipady=130,ipadx=160)

        self.console = scrolledtext.ScrolledText(self.contentRight,  
                            wrap = WORD, width = 53,height = 15,  font = ("Times New Roman", 12))   
        self.console.grid(column = 0, pady = 0, padx = 5)
        #self.console.configure(state ='disabled') 


        #top
        self.contentTop = ttk.Frame(self.frame, padding=(3,3,3,3))
        self.one = ttk.Label(self.contentTop, text="Folder:")

        self.entry_text = StringVar()
        self.folder_path = ttk.Entry(self.contentTop, textvariable=self.entry_text, state='disabled')
        self.browse = ttk.Button(self.contentTop, text="Browse", command=self.browse_button)
        self.generate = ttk.Button(self.contentTop, text="Generate", command=self.generate_button)

        self.one.grid(column=0, row=0)
        self.folder_path.grid(column=1, row=0,columnspan=1,padx=3,ipadx=130)
        self.browse.grid(column=5, row=0)
        self.generate.grid(column=6, row=0, padx=10)

        self.output_text = StringVar()
        self.two = ttk.Label(self.contentTop, text="Output:")
        self.output_path = ttk.Entry(self.contentTop, textvariable=self.output_text, state='disabled')       
        self.two.grid(column=0, row=1)
        self.output_path.grid(column=1, row=1,columnspan=1,padx=3,ipadx=130)

        #left
        self.contentLeft = ttk.Frame(self.frameLeft, padding=(3,3,3,3))
        self.tree = ttk.Treeview(self.contentLeft, show='tree')
        ysb = ttk.Scrollbar(self.contentLeft, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.contentLeft, orient='horizontal', command=self.tree.xview)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        #self.tree.configure(yscrollcommand=lambda f, l:self.autoscroll(ysb,f,l), xscrollcommand=lambda f, l:self.autoscroll(xsb,f,l))
        self.tree.heading('#0', text='Directory Tree:', anchor='w')
        self.tree.column("#0",minwidth=510, stretch=True)
        self.tree.grid(row=0,column=0,ipady=40,ipadx=50)

        #left
        self.contentTop.grid(column=0, row=0,columnspan=2, sticky=(N,E,W), pady=5, padx=5)
        self.contentLeft.grid(column=0, row=1, sticky=(N,E,W), pady=5, padx=5)
        self.contentRight.grid(column=1, row=1, sticky=(N,E,W), pady=5, padx=5)

        #repack
        self.frame.grid(column=0, row=0, columnspan=2, sticky=(N, S, E, W))
        self.frameLeft.grid(column=0, row=1, sticky=(N, S, E, W))
        self.frameRight.grid(column=1, row=1, sticky=(N, S, E, W))

        #final repack
        self.content.grid()

    def traverse_dir(self,parent,path):
        for d in os.listdir(path):
            full_path=os.path.join(path,d)
            isdir = os.path.isdir(full_path)
            id= self.tree.insert(parent,'end',text=d,open=False)
            if isdir:
                self.traverse_dir(id,full_path) 
                

    def browse_button(self):
        #clear treeview
        filename = filedialog.askdirectory()
        for i in self.tree.get_children():
            self.tree.delete(i)
        #generate treeview
        if (filename != ""):
            self.entry_text.set(filename)
            abspath = os.path.abspath(filename)
            node=self.tree.insert('','end',text=filename,open=True)        
            self.traverse_dir(node,abspath)

                

    def generate_button(self):  
        self.console.insert(INSERT, 'Processing... ... ....\n')
        self.console.insert(INSERT, '... ... ....\n')



if __name__ == '__main__':
    root = Tk()
    root.geometry("800x380")
    root.title("TTK GUI Template")
    app = Convert(root, path='')    
    root.mainloop()
