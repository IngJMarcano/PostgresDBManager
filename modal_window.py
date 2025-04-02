import tkinter as tk
from window_utils import set_window_dimensions
from db_utils import create_env_file
from db_utils import test_db_connection
from tkinter import messagebox

class ModalWindow:
    def __init__(self, parent, data_callback):
        self.parent = parent
        self.data_callback = data_callback

        self.new_window = tk.Toplevel(self.parent)
        self.new_window.title('Registrar Base de Datos')
        self.new_window = set_window_dimensions(self.new_window, 0.2, 0.6)
        self.new_window.resizable(False, False)
        self.new_window.grab_set()

        # Formulario
        self.label_host = tk.Label(self.new_window, text='Host:')
        self.label_host.pack(pady=5)
        self.entry_host = tk.Entry(self.new_window)
        self.entry_host.insert(0, 'localhost')
        self.entry_host.pack(pady=5)

        self.label_port = tk.Label(self.new_window, text='Puerto:')
        self.label_port.pack(pady=5)
        self.entry_port = tk.Entry(self.new_window)
        self.entry_port.insert(0, '5432')
        self.entry_port.pack(pady=5)

        self.label_user = tk.Label(self.new_window, text='Usuario:')
        self.label_user.pack(pady=5)
        self.entry_user = tk.Entry(self.new_window)
        self.entry_user.insert(0, 'postgres')
        self.entry_user.pack(pady=5)

        self.label_password = tk.Label(self.new_window, text='Contraseña:')
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.new_window, show='*')
        self.entry_password.pack(pady=5)

        self.label_database = tk.Label(self.new_window, text='Base de Datos:')
        self.label_database.pack(pady=5)
        self.entry_database = tk.Entry(self.new_window)
        self.entry_database.pack(pady=5)

        self.label_identifier = tk.Label(self.new_window, text='Identificador:')
        self.label_identifier.pack(pady=5)
        self.entry_identifier = tk.Entry(self.new_window)
        self.entry_identifier.insert(0, 'prueba')
        self.entry_identifier.pack(pady=5)
        
        button_frame = tk.Frame(self.new_window)
        button_frame.pack(pady=5)


        self.submit_button = tk.Button(button_frame, text='Guardar', command=self.submit_form)
        self.submit_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.close_button = tk.Button(button_frame, text='Cancelar', command=self.close_window)
        self.close_button.pack(side=tk.LEFT, pady=5)

    
    def submit_form(self):
        data = {
            "host" : self.entry_host.get(),
            "port" : self.entry_port.get(),
            "user" : self.entry_user.get(),
            "password" : self.entry_password.get(),
            "database" : self.entry_database.get(),
            "identifier" : self.entry_identifier.get()
        }
        connection_success = test_db_connection(data['database'], data['user'], data['password'], data['host'], data['port'])
        if (not connection_success) :
            messagebox.showinfo('Error', 'No se conecto con la Base de Datos.')
        else : 
            create_env_file(data['identifier'], data['database'], data['user'], data['password'], data['host'], data['port'])
            messagebox.showinfo('Éxito', 'Datos enviados exitosamente.')
            self.data_callback(data)
            self.close_window()

    def close_window(self):
        self.new_window.grab_release()
        self.new_window.destroy()
