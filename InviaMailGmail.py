import smtplib # implementazione in Python del protocollo SMTP, che sta per Simple Mail Transfer Protocol
"""
ATTENZIONE: a seguito dell'aggiornamento delle politiche di sicurezza di Google, per poter utilizzare 
quanto descritto nel tutorial seguente potreste aver bisogno di aggiungere un'eccezzione per 
l'utilizzo di applicazioni esterne dalle impostazioni del vostro account di posta! 
devi andare nella sezione sicurezza dell'account google e disattivare il blocco accesso delle 
App meno sicure """


def postino():
    print("""
    Questa è la funzione Postino: spedisce eMail utilizzando Gmail!
    Server: smtp.gmail.com
    Porta: 587
    Si richiedono: Username, Password, Destinatario, Oggetto e Messaggio da inviare.
    """)

    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    destinatario = input("Inserisci l'email del destinatario: ")
    oggetto = input("Inserisci l'oggetto della mail: ")
    messaggio = input("Ora puoi inserire il messaggio che vuoi inviare: ")
    contenuto = f"Subject: {oggetto}\n\n{messaggio}"
    print("Sto effettuando la connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()  
    email.starttls()  
    
    email.login(username,password)
    print("Sto inviando...")
    email.sendmail(username, destinatario, contenuto)
    email.quit()
    print("Messaggio Inviato!")
    input("")

postino()
