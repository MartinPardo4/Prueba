import tkinter as tk
import calendar

def mostrar_calendario(año, mes):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    calendario_str = cal.formatmonth(año, mes)
    
    # Actualizar el contenido del widget de texto para mostrar el calendario
    calendario_label.config(text=calendario_str)

def actualizar_calendario():
    año = int(año_entry.get())
    mes = int(mes_entry.get())
    mostrar_calendario(año, mes)

# Crear la ventana principal
root = tk.Tk()
root.title("Calendario Mensual")

# Crear widgets de entrada para el año y el mes
año_label = tk.Label(root, text="Año:")
año_label.pack(pady=5)
año_entry = tk.Entry(root)
año_entry.pack(pady=5)

mes_label = tk.Label(root, text="Mes:")
mes_label.pack(pady=5)
mes_entry = tk.Entry(root)
mes_entry.pack(pady=5)

# Crear botón para actualizar el calendario
actualizar_button = tk.Button(root, text="Mostrar Calendario", command=actualizar_calendario)
actualizar_button.pack(pady=10)

# Crear el widget de texto para mostrar el calendario
calendario_label = tk.Label(root, font=("Courier", 14), justify=tk.LEFT)
calendario_label.pack(padx=10, pady=10)

# Ejecutar el bucle principal
root.mainloop()

