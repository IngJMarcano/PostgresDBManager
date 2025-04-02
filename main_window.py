import tkinter as tk
from window_utils import set_window_dimensions
from modal_window import ModalWindow

class MainWindow:
    def __init__(self, root, data_callback):
        self.root = root
        self.data_callback = data_callback
        self.frame = tk.Frame(self.root)
        self.new_window = set_window_dimensions(self.root, 0.5, 0.8)
        self.label = tk.Label(self.frame, text='Ventana Principal')
        self.label.pack(pady=10)
        
        self.open_modal_button = tk.Button(self.frame, text='Abrir Modal', command=self.open_modal)
        self.open_modal_button.pack(pady=5)
        self.frame.pack(fill=tk.BOTH, expand=True)

    def open_modal(self):
        modal = ModalWindow(self.root, self.data_callback)
