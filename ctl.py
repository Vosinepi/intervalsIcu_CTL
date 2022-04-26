import json
import tkinter as tk
from urllib import response
import requests

# datos
api_token = "reemplazar por API_KEY"
id_atleta = "id_atleta"

# request
response = requests.get(
    "https://intervals.icu/api/v1/athlete/i61568/wellness",
    auth=("API_KEY", str(api_token)),
)

# obtencion de CTL y ATL y redondeo a dos decimales
data = response.json()
print(json.dumps(data[-1], indent=4, sort_keys=True))
ctl_largo = float(json.dumps(data[-1]["ctl"], indent=4, sort_keys=True))
atl_largo = float(json.dumps(data[-1]["atl"], indent=4, sort_keys=True))

ctl_corto = round(ctl_largo, 2)
atl_corto = round(atl_largo, 2)

# crear ventana
window = tk.Tk()


# window.attributes('-fullscreen', True)
window.attributes("-alpha", 0.5)
window.geometry("200x210+1720+0")
window.resizable(False, False)
window.update_idletasks()
window.overrideredirect(True)

# crear text label de titulo para CTL
label = tk.Label(window, text="CTL", font=("Arial 15"))
label.pack()

# funcion muestra de CTL
def text(n):
    label = tk.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


text(ctl_corto)

# crear text label de titulo para ATL
label = tk.Label(window, text="ATL", font=("Arial 15"))
label.pack()

# funcion muestra de ATL
def atl(n):
    label = tk.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


atl(atl_corto)

# crear text label de titulo para FORMA
label = tk.Label(window, text="FORMA", font=("Arial 15"))
label.pack()

# funcion FORMA
def forma(n):
    label = tk.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


forma(round((ctl_corto - atl_corto), 2))


window.mainloop()
