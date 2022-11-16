import database as db
from tkinter import *
from tkinter import ttk

class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()
        
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'NOMBRE', 'APELLIDO')

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("NOMBRE", anchor=CENTER)
        treeview.column("APELLIDO", anchor=CENTER)

        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
        treeview.heading("APELLIDO", text="APELLIDO", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeview['yscrollcommand'] = scrollbar.set

        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='',
                index='end',
                iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido)
            )
        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Crear", command=None).grid(row=0, column=0)
        Button(frame, text="Modificar", command=None).grid(row=0, column=1)
        Button(frame, text="Borrar", command=None).grid(row=0, column=2)

        self.treeview = treeview


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
