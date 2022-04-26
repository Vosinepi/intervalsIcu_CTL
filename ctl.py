import json
from tkinter import *
import tkinter
from urllib import response
import requests

# datos
api_token = "api_key"
id_atleta = "ID"

# request
response = requests.get(
    "https://intervals.icu/api/v1/athlete/i61568/wellness",
    auth=("API_KEY", str(api_token)),
)

# obtencion de CTL y ATL y redondeo a dos decimales
data = response.json()
print(json.dumps(data[-1]["ctl"], indent=4, sort_keys=True))
i = -1
semanaCtl = []

while i < 0 and i >= -8:

    semanaCtl.append(json.dumps(data[i]["ctl"], indent=4, sort_keys=True))
    i -= 1
print(semanaCtl)
ctl_largo = float(json.dumps(data[-1]["ctl"], indent=4, sort_keys=True))
atl_largo = float(json.dumps(data[-1]["atl"], indent=4, sort_keys=True))

ctl_corto = round(ctl_largo, 2)
atl_corto = round(atl_largo, 2)

# crear ventana
window = tkinter.Tk()


# window.attributes('-fullscreen', True)
window.attributes("-alpha", 0.5)
window.geometry("150x290+1770+0")
window.resizable(False, False)
window.update_idletasks()
window.overrideredirect(True)

# crear text label de titulo para CTL
label = tkinter.Label(window, text="CTL", font=("Arial 15"))
label.pack()

# funcion muestra de CTL
def text(n):
    label = tkinter.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


text(ctl_corto)

# crear text label de titulo para ATL
label = tkinter.Label(window, text="ATL", font=("Arial 15"))
label.pack()

# funcion muestra de ATL
def atl(n):
    label = tkinter.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


atl(atl_corto)

# crear text label de titulo para FORMA
label = tkinter.Label(window, text="FORMA", font=("Arial 15"))
label.pack()

# funcion FORMA
def forma(n):
    label = tkinter.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


forma(round((ctl_corto - atl_corto), 2))

# crear text label de titulo para RAMPA
label = tkinter.Label(window, text="RAMPA", font=("Arial 15"))
label.pack()

# funcion RAMPA
def rampa(n):
    label = tkinter.Label(text=(str(n)), font="Arial 25", fg="red")
    label.master.overrideredirect(True)
    label.master.lift()

    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()


rampa(round((float(semanaCtl[0]) - float(semanaCtl[7])), 2))

window.mainloop()
