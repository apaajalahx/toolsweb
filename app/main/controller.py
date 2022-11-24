import smtplib as smtp
from smtplib import *
import ssl
from email import message
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

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
        m.add_header('subject', 'Smtp Email Sent Market Inbox')
        m.add_header('X-Priority', '1')
        m.set_payload('Email Received')
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

def sendinblue_send(apikey, sender, content, recipient):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = apikey
    
    api_instances = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
    send_sms = sib_api_v3_sdk.SendTransacSms(sender=sender, recipient=recipient, content=content)
    try:
        resp = api_instances.send_transac_sms(send_sms)
        return { 'error' : False, 
                 'messages' : 'SMS Has been sent.', 
                 'data' : {
                            'recipient' : recipient,
                            'sms_count' : resp.sms_count,
                            'used_credits' : resp.used_credits,
                            'remaining_credits' : resp.remaining_credits
                         }
                }
    except ApiException as e:
        return {
            'error' : True,
            'messages' : 'Failed send SMS, APIKEY DIE'
        }

def sendinblue_check(apikey):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = apikey
    api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))
    credits = 0
    try:
        api_response = api_instance.get_account()
        for data in api_response.plan:
            if 'sms' in data.type:
                credits = data.credits
        return {
            'error' : False,
            'messages' : 'API KEY LIVE',
            'data' : {
                'api_key' : apikey,
                'sms_credits' : credits
            }
        }
    except:
        return {
            'error' : True,
            'messages' : 'API KEY DIE'
        }
