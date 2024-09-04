import tkinter as tk
from tkinter import messagebox


class SalaryCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Sueldo")

        # Etiqueta y entrada para el saldo actual
        self.label = tk.Label(root, text="Dame saldo actual:")
        self.label.grid(row=0, column=0)
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1)

        # Botón para calcular el saldo final
        self.calculate_button = tk.Button(root, text="Calcular Saldo", command=self.calculate_salary)
        self.calculate_button.grid(row=1, column=0, columnspan=2)

    def calculate_salary(self):
        try:
            initial_balance = float(self.entry.get())

            if initial_balance < 1000.00:
                final_balance = initial_balance * (1 + 0.03)
            else:
                final_balance = initial_balance * (1 + 0.04)

            messagebox.showinfo("Saldo Final", f"Saldo final es: {final_balance:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryCalculatorApp(root)
    root.mainloop()