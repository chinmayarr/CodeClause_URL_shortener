import pyshorteners as shortner
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
ctk.set_widget_scaling(1)
ctk.set_window_scaling(4)
#styles

def button_press():
    url=srcurl.get()
    s=shortner.Shortener()
    short_url=s.tinyurl.short(url)
    outputlabel=ctk.CTkLabel(master=frame,text="Shortened url is:")
    outputlabel.pack(padx=5,pady=(50,0))
    output=ctk.CTkTextbox(master=frame,height=10,width=400)
    output.pack(pady=(10,0),side="top")
    output.insert(ctk.END,short_url)
    

interface=ctk.CTk()
interface.title("URL-Shortner")
interface.geometry("150x100")
frame=ctk.CTkFrame(master=interface)
frame.pack(padx=60,pady=10,fill="both",expand=True)
label=ctk.CTkLabel(master=frame,text="Enter the original url")
label.pack(padx=5)
srcurl=ctk.CTkEntry(master=frame,placeholder_text="url")
srcurl.pack(padx=12,pady=10)
btn=ctk.CTkButton(master=frame,text="Shorten url",command=button_press)
#button style

btn.pack()
interface.mainloop()