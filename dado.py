import tkinter as tk
import random

def arrojar_dado():
    caja_dado.config(state=tk.NORMAL)       # Activar la caja para editar
    caja_dado.delete(0, tk.END)             # Borrar contenido anterior
    valor = random.randint(1, 6)            # Generar valor aleatorio del dado
    caja_dado.insert(0, valor)              # Mostrar resultado
    caja_dado.config(state=tk.DISABLED)     # Desactivar la caja para evitar escritura

# Lado gráfico

ventana = tk.Tk()
ventana.title("Dado 2.0")
ventana.config(width=300, height=300)
ventana.resizable(False, False)

tk.Button(text="Arrojar el dado", command=arrojar_dado).place(x=90, y=50, width=120, height=60)
tk.Label(text="Valor:").place(x=90, y=130)

caja_dado = tk.Entry(state=tk.DISABLED)
caja_dado.place(x=90, y=160, width=50, height=25)

ventana.mainloop()
