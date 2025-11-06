import os
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.


class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv("ACCOUNTSID"), os.getenv("AUTHTOKEN"))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            messaging_service_sid=str(os.getenv("messagesid")),
            body=message_body,
            from_='+12297017683',
            to=str(os.getenv("MYNUMBER"))
        )
        print(message.status)
        print(message.sid)
