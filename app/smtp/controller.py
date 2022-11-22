import smtplib as smtp
from smtplib import *
import ssl
from email import message

def smtp_check(host, port, username, password, email_to, email_from):
    try:
        m = message.Message()
        emailfrom = email_from
        if email_from is None:
            if '@' in username:
                emailfrom = username
            else:
                emailfrom = 'noreply@market-inbox.com'
        m.add_header('from', emailfrom)
        m.add_header('to', email_to)
        m.add_header('subject', 'Market Inbox Test SMTP')
        m.add_header('X-Priority', '1')
        m.set_payload('THIS JUST TEST! SMTP SEND THIS SMTP GOOD FOR YOU !')
        if port == 465:
            context = ssl.create_default_context()
            server = smtp.SMTP_SSL(host, port, context=context)
        else:
            server = smtp.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(emailfrom, email_to, m.as_string())
        server.quit()
        return { 'error' : False, 'messages' : 'succes send mail!' }
    except SMTPAuthenticationError:
        return { 'error' : True, 'messages' : 'SMTP Authentication Error' }
    except SMTPConnectError:
        return { 'error' : True, 'messages' : 'SMTP Connect Error' }
    except SMTPServerDisconnected:
        return { 'error' : True, 'messages' : 'SMTP Server Disconnected' }
    except SMTPRecipientsRefused:
        return { 'error' : True, 'messages' : 'Recipients Refused' }
    except:
        return { 'error' : True, 'messages' : 'Unkown Error' }