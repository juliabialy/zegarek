import tkinter as tk
from time import strftime

window = tk.TK()
label = tk.Label(window, text = strftime("%H:%M:%S"), font= ("Tahoma",140))

def ref():
    label.config(text=strftime("%H:%M:%S"))
    
button = tk.Button(window, text = "odśwież", command = ref, font= ("Tahoma",40) )


label.pack(side=tk.TOP)
button.pack(side=tk.BOTTOM)
tk.mainloop()
