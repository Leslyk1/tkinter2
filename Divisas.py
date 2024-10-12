import tkinter as tk

# Tasas de conversión fijas
tasas_conversion = {
    'USD': {'EUR': 0.85, 'GBP': 0.74, 'JPY': 110.17},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'JPY': 129.55},
    'GBP': {'USD': 1.36, 'EUR': 1.14, 'JPY': 147.85},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068}
}

# Función que realiza las conversiones
def calcular_conversion():
    divisa_origen = combo_origen.get()
    divisa_destino = combo_destino.get()
    try:
        cantidad = float(entrada_cantidad.get())

        if divisa_origen != divisa_destino:
            tasa = tasas_conversion[divisa_origen][divisa_destino]
            resultado = cantidad * tasa
            etiqueta_resultado.config(text=f"{cantidad:.2f} {divisa_origen} son {resultado:.2f} {divisa_destino}")
        else:
            etiqueta_resultado.config(text="Las divisas de origen y destino deben ser diferentes")
    except ValueError:
        etiqueta_resultado.config(text="Ingrese un valor numérico válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Divisas")

# Crear etiquetas y colocarlas en la cuadrícula
etiqueta_origen = tk.Label(ventana, text="Divisa de origen:")
etiqueta_origen.grid(row=0, column=0, padx=10, pady=10)

etiqueta_destino = tk.Label(ventana, text="Divisa de destino:")
etiqueta_destino.grid(row=1, column=0, padx=10, pady=10)

etiqueta_cantidad = tk.Label(ventana, text="Cantidad:")
etiqueta_cantidad.grid(row=2, column=0, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Crear combo boxes para seleccionar las divisas de origen y destino
divisas = list(tasas_conversion.keys())
combo_origen = tk.StringVar()
combo_origen.set(divisas[0])  # Establece el valor predeterminado
combo_destino = tk.StringVar()
combo_destino.set(divisas[1])  # Establece el valor predeterminado

listado_origen = tk.OptionMenu(ventana, combo_origen, *divisas)
listado_destino = tk.OptionMenu(ventana, combo_destino, *divisas)

listado_origen.grid(row=0, column=1, padx=10, pady=10)
listado_destino.grid(row=1, column=1, padx=10, pady=10)

# Crear campo de entrada para la cantidad 
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.grid(row=2, column=1, padx=10, pady=10)

# Crear botón de conversión 
boton_convertir = tk.Button(ventana, text="Convertir", command=calcular_conversion)
boton_convertir.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la aplicación 
ventana.mainloop()
