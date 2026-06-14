import customtkinter as ctk

print("TEST START")

app = ctk.CTk()
app.geometry("300x200")

label = ctk.CTkLabel(app, text="Hello UI")
label.pack()

app.mainloop()