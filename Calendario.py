import tkinter as tk
import calendar

def mostrar_calendario(año, mes):
    # Limpiar el frame del calendario
    for widget in calendario_frame.winfo_children():
        widget.destroy()
    
    # Crear el calendario
    cal = calendar.Calendar(calendar.SUNDAY)
    días_semana = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
    
    # Añadir los días de la semana a la primera fila
    for idx, día in enumerate(días_semana):
        lbl = tk.Label(calendario_frame, text=día, padx=10, pady=5, font=("Arial", 10, "bold"))
        lbl.grid(row=0, column=idx)
    
    # Obtener las fechas del mes
    fechas = cal.monthdayscalendar(año, mes)
    
    # Añadir las fechas a la grilla
    for semana_idx, semana in enumerate(fechas):
        for día_idx, día in enumerate(semana):
            if día == 0:
                lbl = tk.Label(calendario_frame, text="", padx=10, pady=5)
            else:
                lbl = tk.Label(calendario_frame, text=str(día), padx=10, pady=5)
            lbl.grid(row=semana_idx + 1, column=día_idx)

def actualizar_calendario():
    año = int(año_entry.get())
    mes = int(mes_entry.get())
    mostrar_calendario(año, mes)

# Crear la ventana principal
root = tk.Tk()
root.title("Calendario Mensual")
root.resizable(False, False)

# Crear un frame para los widgets de entrada y el botón
input_frame = tk.Frame(root)
input_frame.pack(padx=30, pady=30)

# Crear widgets de entrada para el año y el mes dentro del frame
año_label = tk.Label(input_frame, text="Año:")
año_label.grid(row=0, column=0, pady=5, padx=5)
año_entry = tk.Entry(input_frame)
año_entry.grid(row=0, column=1, pady=5, padx=5)

mes_label = tk.Label(input_frame, text="Mes:")
mes_label.grid(row=1, column=0, pady=5, padx=5)
mes_entry = tk.Entry(input_frame)
mes_entry.grid(row=1, column=1, pady=5, padx=5)

# Crear botón para actualizar el calendario dentro del frame
actualizar_button = tk.Button(input_frame, text="Mostrar Calendario", command=actualizar_calendario)
actualizar_button.grid(row=2, column=0, columnspan=2, pady=10)

# Crear un frame para el calendario
calendario_frame = tk.Frame(root)
calendario_frame.pack(padx=10, pady=10)

# Ejecutar el bucle principal
root.mainloop()

