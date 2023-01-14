import sys
from inbox_check import daily_inbox_check
from twilio.rest import Client

args = sys.argv

# Loading in Github secrets
account_sid = args[1]
auth_token = args[2]
twilio_phone = args[3]
my_phone = args[4]

response = daily_inbox_check()

client = Client(account_sid, auth_token)

if response is not True:
    client.messages.create(
        body="You still need to muster. You can access the muster page at the \
            following link: https://forms.gle/RJRUCWYVro5Qu62y6.",
        from_=twilio_phone,
        to=my_phone
    )
else:
    client.messages.create(
        body="You've mustered. View your response at the following link: \
            https://forms.gle/RJRUCWYVro5Qu62y6.",
        from_=twilio_phone,
        to=my_phone
    )
