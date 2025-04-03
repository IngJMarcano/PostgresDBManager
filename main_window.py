import os
import tkinter as tk
from window_utils import set_window_dimensions
from db_utils import test_db_connection
from create_window import CreateWindow
from tkinter import ttk, messagebox
import psycopg2
from dotenv import load_dotenv

class MainWindow:
    def __init__(self, root, data_callback):
        self.root = root
        self.data_callback = data_callback
        self.frame = tk.Frame(self.root)
        self.new_window = set_window_dimensions(self.root, 0.5, 0.8)
        self.label = tk.Label(self.frame, text='Ventana Principal')
        self.label.pack(pady=10)
        
        
        self.frame_menu = tk.Frame(self.root)
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)
        self.frame_menu.pack(fill=tk.BOTH, expand=True)

        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        self.create_record_button = tk.Button(self.frame_menu, text='Registrar Base de Datos', command=self.create_record)
        self.create_record_button.pack(side=tk.TOP)
        
        self.btn_open = tk.Button(self.frame_menu, text="Abrir Ventana", command=self.open_window)
        self.btn_open.pack(side=tk.TOP)

        self.btn_edit = tk.Button(self.frame_menu, text="Editar", command=self.edit_record, state=tk.DISABLED)
        self.btn_edit.pack(side=tk.TOP)
        
        
        self.tree = ttk.Treeview(self.frame_list, columns=("identificador", "nombre", "host", "estado"), show='headings')
        self.tree.heading("identificador", text="Identificador", anchor='center')
        self.tree.heading("nombre", text="Nombre", anchor='center')
        self.tree.heading("host", text="Host", anchor='center')
        self.tree.heading("estado", text="Estado", anchor='center')
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.tree.tag_configure("conectado", foreground="green")
        self.tree.tag_configure("desconectado", foreground="red")

        self.tree.bind("<ButtonRelease-1>", self.on_select)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for filename in os.listdir("config"):
            if filename.endswith(".env"):
                env_path = os.path.join("config", filename)
                load_dotenv(env_path)

                db_name = os.getenv("DB_NAME")
                db_user = os.getenv("DB_USER")
                db_password = os.getenv("DB_PASSWORD")
                db_host = os.getenv("DB_HOST")
                db_port = os.getenv("DB_PORT")

                status_bool = test_db_connection(db_name, db_user, db_password, db_host, db_port)
                
                tag = "conectado" if status_bool else "desconectado"
                status = "Connected" if status_bool else "Disconnected"
                self.tree.insert("", "end", values=(filename[:-4], db_name, db_host, status), tags=(tag,))

    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.btn_edit.config(state=tk.NORMAL)
        else:
            self.btn_edit.config(state=tk.DISABLED)
        

    def create_record(self):
        create_modal = CreateWindow(self.root, self.data_callback)
        self.load_data()

    def open_window(self):
        messagebox.showinfo("Info", "Ventana abierta")

    def edit_record(self):
        messagebox.showinfo("Edit", "Editar registro")
        
        
    def check_connection(self, db_name, db_user, db_host, db_port):
        try:
            conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, port=db_port)
            conn.close()
            return "Connected"
        except Exception:
            return "Disconnected"