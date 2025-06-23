import csv
import smtplib as SMTP
import re
from email.message import EmailMessage
from customtkinter import *

fieldnames = ['email', 'name']

SENDER = "youremailhere@gmail.com"
title = ""
content = ""


# connects to the SMTP server
server = SMTP.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(SENDER, "your_password")

# removes an email adress
def remove_email():
    inp1 = CTkInputDialog(text="insira o endereço do email para remover")
    res1 = inp1.get_input()

    removed = False
    wrt = []

    with open("csv/email.csv", "r", newline="", encoding="utf-8") as file:

        data = csv.DictReader(file)
        print(data)
        print(res1)
        for row in data:
            if row["email"] == res1:
                removed = True
            else:
                wrt.append(row)
                print(row)

    with open("csv/email.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(wrt)
    
    return removed
# adds an email adress
def add_email():
    inp2 = CTkInputDialog(text="insira o endereço de email para adicionar")
    res2 = inp2.get_input()

    mask = r"^[^@]+@[^@]+\.[^@]+$"
    res2 = re.findall(mask, res2)

    inp3 = CTkInputDialog(text="insira o nome do destinatario")
    res3 = inp3.get_input()

    if res2 == []:
        return False

    data = {"email": res2[0], "name": res3}

    with open("csv/email.csv", "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)

    return True

# edits the text of the message
def edit_text():

    inp4 = CTkInputDialog(text="insira o titulo do email para enviar")
    global title
    title = inp4.get_input()

    inp5 = CTkInputDialog(text="insira o conteudo do texto. use \\n para pular linhas. caracteres especiais não funcionam :(")
    global content
    content = inp5.get_input()

    content = content.encode().decode("unicode_escape")
# send all the emails to the adresses
def send_emails():

    with open("csv/email.csv", newline="", encoding="utf-8") as csvfile:
        
        global title
        global content

        data = csv.DictReader(csvfile)

        err = False

        for row in data:
            msg = EmailMessage()
            msg['From'] = SENDER
            msg['To'] = row["email"]
            msg['Subject'] = title
            msg.set_content(content, charset="utf-8")

            print("enviando email para " + row["name"])

            result = server.send_message(msg)

            if result:
                print("nao foi possivel enviar o email. codigo de erro:", result)
                err = True
            else:
                print("email enviado com sucesso")
                print()
        return err