import customtkinter
app = customtkinter.CTk()
app.title('Babybenzz')
app.geometry('500x500')

label = customtkinter.CTkLabel(app, text='boo', fg_color='#F08080',  font='aria', 29)
label.pack(pady=(20, 0))

entry = customtkinter.CTkEntry(app, placeholder_text='Hello boo')
entry.pack(pady=(20, 0))

app.mainloop()
