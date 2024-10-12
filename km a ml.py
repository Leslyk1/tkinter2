import tkinter as tk

def convertir():
    try:
        #Obtener el valor ingresado en el campo de entrada
        kilometros = float(entrada_kilometros.get())

        #Realiza la conversion a millas (1 kilometro = 0.621371 millas)
        millas = kilometros * 0.621371

        #Actualiza la etiqueta de resultado
        etiqueta_resultado.config(text=f"{kilometros} kilometros son {millas} millas")
    except ValueError:
        #Manejo de errores para entardas no validas
        etiqueta_resultado.config(text="Ingrese un valor numerico valido")

 # Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de kilometros a Millas")
ventana.geometry("300x150") #Establece el tamaño de la ventana

# Crear etiqueta de instruccion y colocar en la cuadricula
etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en kilometros: ")
etiqueta_instruccion.grid(row=0, column=0, padx=10, pady=10)

# crear campo de entrada y colocarlo en la cuadricula
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

# crear boton de converion y colocarlo en la cuadricula 
boton_convertir = tk.Button(ventana, text= "Convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

#Crear etiqueta de resultado y colocarla en la cuadricula
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#Iniciar la aplicacion 
ventana.mainloop()