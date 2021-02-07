from email.message import EmailMessage
import smtplib
import imghdr
import os
import datetime
"""
Questo programma serve a me per autoinviarmi al mio account hotmail gli screenshoot dei programmi realizzati
in giornata. La directory è sempre C:\\Users\\Federico\\Desktop\\Guide\\Python,dove sono presenti gli screen
"""

oggi=str(datetime.datetime.now())

def finder():
    percorso=r"C:\Users\Federico\Desktop\Guide\Python"
    file_allegare = []
    for cartella,sottocartelle,files in os.walk(percorso):
        for file in files:
            if file.endswith(".JPG") or file.endswith(".jpg"):
                file_controllare=os.path.join(cartella,file)
                data_file = datetime.datetime.fromtimestamp(os.path.getmtime(file_controllare))
                data=str(data_file)
                if data[0:10] == oggi[0:10]:    #se la data è uguale ad oggi
                    file_allegare.append(os.path.join(cartella,file))
    return file_allegare

def postino(lista_file):
    msg = EmailMessage()   
    msg['Subject'] = "SCREENSHOOT"
    msg['From'] = "fedemilani.89@hotmail.it"
    msg['To'] = "fedemilani.89@hotmail.it"
    if lista_file != []:
        for file in lista_file:
            with open(file, 'rb') as fp:
                img_data = fp.read() 
                msg.add_attachment(img_data, maintype='image',subtype=imghdr.what(None, img_data))
    else:    
        print("Non ci sono file di oggi da inviare!")
        input("")
        return None
    # Send the email via our own SMTP server.
    email=smtplib.SMTP("smtp.live.com", 25)
    email.ehlo()    #connessione al server
    email.starttls()  #crittografia TLS
    email.login("fedemilani.89@hotmail.it","FedeGiadiTobiLugna4")
    print("Sto inviando...")
    email.send_message(msg) 
    email.quit()  
    print("Messaggio Inviato!")
    input("")

file_da_allegare=finder()
postino(file_da_allegare)
