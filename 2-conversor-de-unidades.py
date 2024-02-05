import tkinter as tk
from tkinter import Entry, Button, Label, StringVar

class ConversorUnidades:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Unidades")

        self.valor_entrada = StringVar()
        self.resultado_var = StringVar()

        # Etiqueta y entrada para el valor a convertir
        Label(root, text="Valor a Convertir:").grid(row=0, column=0, padx=10, pady=10)
        Entry(root, textvariable=self.valor_entrada).grid(row=0, column=1, padx=10, pady=10)

        # Botones para seleccionar las conversiones
        Button(root, text="Celsius a Fahrenheit", command=lambda: self.convertir_temperatura('Celsius a Fahrenheit')).grid(row=1, column=0, columnspan=2, pady=10)
        Button(root, text="Fahrenheit a Celsius", command=lambda: self.convertir_temperatura('Fahrenheit a Celsius')).grid(row=2, column=0, columnspan=2, pady=10)
        Button(root, text="Metros a Pies", command=lambda: self.convertir_longitud('Metros a Pies')).grid(row=3, column=0, columnspan=2, pady=10)
        Button(root, text="Pies a Metros", command=lambda: self.convertir_longitud('Pies a Metros')).grid(row=4, column=0, columnspan=2, pady=10)
        Button(root, text="Litros a Galones", command=lambda: self.convertir_capacidad('Litros a Galones')).grid(row=5, column=0, columnspan=2, pady=10)
        Button(root, text="Galones a Litros", command=lambda: self.convertir_capacidad('Galones a Litros')).grid(row=6, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado de la conversión
        Label(root, text="Resultado:").grid(row=7, column=0, padx=10, pady=10)
        Entry(root, textvariable=self.resultado_var, state='readonly').grid(row=7, column=1, padx=10, pady=10)

    def convertir_temperatura(self, conversion):
        try:
            valor = float(self.valor_entrada.get())
            if conversion == 'Celsius a Fahrenheit':
                resultado = (valor * 9/5) + 32
            elif conversion == 'Fahrenheit a Celsius':
                resultado = (valor - 32) * 5/9
            self.resultado_var.set(f"{valor} {conversion.split(' a ')[0]} es {resultado:.2f} {conversion.split(' a ')[1]}")
        except ValueError:
            self.resultado_var.set("Error: Valor no válido")

    def convertir_longitud(self, conversion):
        try:
            valor = float(self.valor_entrada.get())
            if conversion == 'Metros a Pies':
                resultado = valor * 3.281
            elif conversion == 'Pies a Metros':
                resultado = valor / 3.281
            self.resultado_var.set(f"{valor} {conversion.split(' a ')[0]} es {resultado:.2f} {conversion.split(' a ')[1]}")
        except ValueError:
            self.resultado_var.set("Error: Valor no válido")

    def convertir_capacidad(self, conversion):
        try:
            valor = float(self.valor_entrada.get())
            if conversion == 'Litros a Galones':
                resultado = valor / 3.785
            elif conversion == 'Galones a Litros':
                resultado = valor * 3.785
            self.resultado_var.set(f"{valor} {conversion.split(' a ')[0]} es {resultado:.2f} {conversion.split(' a ')[1]}")
        except ValueError:
            self.resultado_var.set("Error: Valor no válido")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorUnidades(root)
    root.mainloop()
