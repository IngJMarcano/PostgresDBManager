import tkinter as tk
import json
from main_window import MainWindow

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Postgres DataBase Manager')
        self.main_window = MainWindow(self.root, self.on_data_received)

    def on_data_received(self, data):
        print('Datos recibidos:', json.dumps(data, indent=4))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
