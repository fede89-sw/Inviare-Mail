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
    file_allegare = [] #array con il percorso di ogni file da allegare
    for cartella,sottocartelle,files in os.walk(percorso):
        for file in files:
            if file.endswith(".JPG") or file.endswith(".jpg"): #mi interessano solo i JPG
                file_controllare=os.path.join(cartella,file) #file nella cartella da controllare la data
                data_file = datetime.datetime.fromtimestamp(os.path.getmtime(file_controllare))#data file
                data=str(data_file) #trasformo in stringa
                if data[0:10] == oggi[0:10]:    #se la data è uguale ad oggi
                    file_allegare.append(os.path.join(cartella,file)) #salvo il xcorso file nell'array
    return file_allegare    #ritorno il file

def postino(lista_file):
    msg = EmailMessage()        # Create the container email message.
    msg['Subject'] = "SCREENSHOOT"
    msg['From'] = "fedemilani.89@hotmail.it" #mittente
    msg['To'] = "fedemilani.89@hotmail.it"  #destinatario
    if lista_file != []:
        for file in lista_file:
            with open(file, 'rb') as fp: #apre il file img dell'array da allegare nella variabile fp
                img_data = fp.read()    #metto il file img in img_data
                msg.add_attachment(img_data, maintype='image',subtype=imghdr.what(None, img_data))
    else:                   #allego il file img e con imghdr controllo che tipo di file img sia(JPEG,PNG)
        print("Non ci sono file di oggi da inviare!") # se array da allegare vuoto,esco
        input("")
        return None
    # Send the email via our own SMTP server.
    email=smtplib.SMTP("smtp.live.com", 25) #server e port Hotmail
    email.ehlo()    #connessione al server
    email.starttls()  #crittografia TLS
    email.login("fedemilani.89@hotmail.it","FedeGiadiTobiLugna4") #mie credenziali Hotmail
    print("Sto inviando...")
    email.send_message(msg) #invia mail con allegato
    email.quit()        #chiude connessione
    print("Messaggio Inviato!")
    input("")

file_da_allegare=finder()
postino(file_da_allegare)
