import mails
from customtkinter import *

window = CTk()
window.geometry("650x500")
window.resizable(width=False, height=False)

font1 = CTkFont("Arial", 30)
font2 = CTkFont("Arial", 14)
font3 = CTkFont("Arial", 20)

# these functions are used on the buttons so they can call the actual function

def rem_mail():
    res = mails.remove_email()
    if res == True:
        output.configure(text="email removido com sucesso")
        return
    output.configure(text="email nao existente")

def add_mail():
    res = mails.add_email()

    if res == False:
        output.configure(text="email invalido")
        return

    output.configure(text="email adicionado com sucesso")

def edit_mail():
    mails.edit_text()
    output.configure(text="email editado com sucesso")

def send_mail():
    res = mails.send_emails()
    if res == False:
        output.configure(text="emails enviados com sucesso")
        return
    output.configure(text="alguns ou todos os emails tiveram erro")


# main GUI

title = CTkLabel(window, width=500, height=50, text="o que você deseja fazer?", font=font1)
title.place(x=75, y=200)

bt_remove = CTkButton(window, width=130, height=50, command=rem_mail, text="remover um email", fg_color="#4e4e52", hover_color="gray", border_color="#bfbfc7", border_width=1.5, text_color="#cfcfcf", font=font2)
bt_remove.place(x=40, y=300)

bt_add = CTkButton(window, width=130, height=50, command=add_mail, text="adicionar um email", fg_color="#4e4e52", hover_color="gray", border_color="#bfbfc7", border_width=1.5, text_color="#cfcfcf", font=font2)
bt_add.place(x=260, y=300 )

bt_edit = CTkButton(window, width=130, height=50, command=edit_mail, text="editar o conteudo", fg_color="#4e4e52", hover_color="gray", border_color="#bfbfc7", border_width=1.5, text_color="#cfcfcf", font=font2)
bt_edit.place(x=480, y=300)

bt_send = CTkButton(window, width=130, height=50, command=send_mail, text="enviar", fg_color="#4e4e52", hover_color="gray", border_color="#bfbfc7", border_width=1.5, text_color="#cfcfcf", font=font3)
bt_send.place(x=260, y=400)

output = CTkLabel(window, width=500, height=50, text="", font=font1)
output.place(x=75, y = 50)

window.mainloop()

