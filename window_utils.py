from tkinter import filedialog
from tkinter import messagebox

def set_window_dimensions(new_window, width_factor=0.3, height_factor=0.4):
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    width = int(screen_width * width_factor)
    height = int(screen_height * height_factor)
    new_window.geometry(f'{width}x{height}')

    return new_window


def save_text_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write('Este es el contenido del archivo de texto.')
            messagebox.showinfo('Éxito', 'Archivo guardado exitosamente.')
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo guardar el archivo: {e}')
