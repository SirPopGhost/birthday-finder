from twilio.rest import Client
import os 

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_sms(phone_reciept):
  for birth_loop in phone_reciept:
    message = client.messages.create(
    from_=os.getenv('FROM'),
    body=f'This is a message from Srikar using twilio. Hello {birth_loop[0]}, I am using an api to send a sms message to you. Thank you for supporting in my coding journey.',
    to=birth_loop[1],
  )
  print(message.sid)



