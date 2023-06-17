import customtkinter
app = customtkinter.CTk()
app.title('Babybenzz')
app.geometry('500x500')

label = customtkinter.CTkLabel(app, text='boo', fg_color='#F08080',  font=('aria', 29))
label.pack(pady=(20, 0))

answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('aria', 30))
answer_label.pack(pady=(20, 0))

entry = customtkinter.CTkEntry(app, placeholder_text='Hello boo')
entry.pack(pady=(20, 0))

def button_event():
    user_input = entry.get()
    answer = eval(user_input)
    answer_text.set(answer)
    print(user_input, answer)

botton = customtkinter.CTkButton(app, text="ปี๊ปๆ", command=button_event)
botton.pack(pady=(20, 0))

app.mainloop()
