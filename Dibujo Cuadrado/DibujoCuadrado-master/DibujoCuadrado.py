import tkinter as tk
from tkinter import simpledialog


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        resultado = ""
        # Dibuja el lado superior
        resultado += '*' * self.lado + '\n'

        # Dibuja los lados laterales
        for i in range(self.lado - 2):
            resultado += '*' + ' ' * (self.lado - 2) + '*' + '\n'

        # Dibuja el lado inferior
        resultado += '*' * self.lado + '\n'
        return resultado


def mostrar_cuadrado():
    N = simpledialog.askinteger("Input", "Introduce el número de asteriscos para cada lado del cuadrado:")
    if N and N > 1:
        cuadrado = Cuadrado(N)
        resultado = cuadrado.dibujar()
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, resultado)
        text_area.config(state=tk.DISABLED)
    else:
        tk.messagebox.showerror("Error", "Introduce un número mayor que 1.")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Dibujo de Cuadrado")

# Botón para mostrar el cuadrado
boton = tk.Button(root, text="Dibujar Cuadrado", command=mostrar_cuadrado)
boton.pack(pady=10)

# Área de texto para mostrar el cuadrado
text_area = tk.Text(root, height=20, width=40, state=tk.DISABLED)
text_area.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()