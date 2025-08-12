import smtplib
import ssl
from email.message import EmailMessage

sender_email="dataautomation.py@gmail.com"
app_password = "bysrdzjryxrlaluo"
recipients=[{"email": "raydit.business@gmail.com", "name":"elvish"},{"email":"aimers.student05@gmail.com","name":"bikas "}]
 
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(sender_email,app_password)
    for person in recipients:
        email=EmailMessage()
        email['from']=sender_email
        email['to']=person["email"]
        email['subject']=f"hello {person['name']}! you have a message from ashis"
        body=f"""
        Hii {person['name']},
        how are you, is everything fine there. 

        regards 
        ashis
        """
        email.set_content(body)

        smtp.send_message(email)

print (" oojii paaaajiii doonee jii")