import leglight
light = None
from tkinter import *
from tkinter import messagebox


def set_ip(value):
    global light
    ip_address = ip_entry_fld.get()
    try:
        light = leglight.LegLight(ip_address, 9123)
        btn['state'] = 'disabled'
        btn['text'] = 'Connected'
        print("Connected")
    except:
        messagebox.showerror("Error", "Not able to connect")


def set_brightness(brightness_val):
    print(f"brightness")
    if light:
        light.brightness(int(brightness_val))
    #else:
    #    messagebox.showerror("Error", "No device connected")


def set_colour(colour_val):
    if light:
        light.color(int(colour_val))
    #else:
    #    messagebox.showerror("Error", "No device connected")


window=Tk()
btn=Button(window, text="Connect", fg='blue')
btn.place(x=200, y=40)
btn.bind("<Button-1>", set_ip)
title=Label(window, text="Keylight Controller", fg='black', font=("Helvetica", 16))
title.place(x=60, y=10)

ip_entry_fld=Entry(window, text="", bd=2)
ip_entry_fld.insert(END, '10.0.12.169')
ip_entry_fld.place(x=20, y=40)

brightness_lbl=Label(window, text="Brightness", fg='black', font=("Helvetica", 13))
brightness_lbl.place(x=60, y=90)

brightness_slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_brightness)
brightness_slider.place(x=60, y=110)

colour_lbl=Label(window, text="Colour", fg='black', font=("Helvetica", 13))
colour_lbl.place(x=60, y=160)

colour_slider = Scale(window, from_=2900, to=7000, orient=HORIZONTAL, command=set_colour)
colour_slider.place(x=60, y=180)


window.title('Keylight Controller')
window.geometry("300x230+10+10")
window.mainloop()