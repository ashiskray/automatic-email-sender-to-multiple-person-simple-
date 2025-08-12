# automatic-email-sender-to-multiple-person-simple-
This is the simple python script to send automatic simple email to multiple persons.


## How It Works  
1. Import required modules:  
   - ssl → For secure connection  
   - smtplib → Send email via SMTP  
   - EmailMessage → Create and format email  
     

2. Create an email object and set:  
   - From, To, Subject, Content  


4. Connect and send:  
   - Uses Gmail’s SMTP server with SSL (smtp.gmail.com, port 465)  
   - Logs in with *App Password*  
   - Sends the email  


## Additional information
* Provide the email id of the sender
* Provide the email id of the receiver
* Done 2-step verification in senders mail
* Make app password in google app password and use this password

# Demerits of this code 
- Every person in the list of multiple person can see that the same mail is send to whom
- E-mail id of the every persons will be reveiled.
  
  
