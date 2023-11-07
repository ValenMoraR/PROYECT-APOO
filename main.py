import os
from code_1 import tk, Reproductor

ventana = tk.Tk()
ventana.geometry("800x300")
# ventana.resizable(width=0, height=0)
if os.path.exists("favoritos.json"):
    os.remove("favoritos.json")

reproductor = Reproductor(ventana)
if __name__ == "__main__": 
    ventana.mainloop()
