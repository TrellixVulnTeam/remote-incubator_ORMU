from myPackage.mail import *

def sendMailTo(receiver_email_id):
    try:
        my_email = email
        my_pass = email_pass

        receiver_email =receiver_email_id

        subject = 'Thank you for get registered in remote incubator'
        message = '''
                    This mail is auto-generated mail and should not be replied back.
                    Hassan Bari Raza, Machine learning enthusiast working at Fame Technologies has
                    created this auto-generated mail system.
                    Your data has been added to the remote incubator database.
                    '''
        # instantiate a multipart class
        msg = MIMEMultipart()

        msg['FROM'] = my_email
        msg['TO'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message,'plain'))
    
        # login to the gmail server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        print("server connected")
        server.starttls()
        print("connected in tls mode")
        server.login(my_email, my_pass)
        print("login successful")
        text = msg.as_string()
        print("text: ",text)
        server.sendmail(my_email, receiver_email, text)
        print("mail sent")
        server.quit()
        print("connection closed")

        return "email sent, successfully"
    except Exception as e:
        print("not sent to receiver mail address")