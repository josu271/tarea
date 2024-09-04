import tkinter as tk
from tkinter import messagebox


class GradeEvaluatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluador de Calificaciones")

        # Etiqueta y entrada para la calificación
        self.label = tk.Label(root, text="Ingresa la calificación:")
        self.label.grid(row=0, column=0)
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1)

        # Botón para evaluar la calificación
        self.evaluate_button = tk.Button(root, text="Evaluar", command=self.evaluate_grade)
        self.evaluate_button.grid(row=1, column=0, columnspan=2)

    def evaluate_grade(self):
        try:
            grade = float(self.entry.get())
            grade_letter = self.get_grade_letter(grade)
            messagebox.showinfo("Resultado", f"La calificación es {grade_letter}.")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

    def get_grade_letter(self, grade):
        if grade > 9.0:
            return "A"
        elif grade > 8.0:
            return "B"
        elif grade >= 7.5:
            return "C"
        else:
            return "R"


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeEvaluatorApp(root)
    root.mainloop()