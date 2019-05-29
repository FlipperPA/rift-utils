import smtplib

import requests


# Enter your email address here. You can often email your mobile phone.
# For example, with Verizon, you can send a text by emailing `phonenumber@vtext.com`
sender = 'youremail@yourdomain.org'
receivers = ['youremail@yourdomain.com']

# Enter the Zone Events you want to track here
events = [
    'Critical Mass',
    'Inner Maelstrom',
    'Melting Point',
    'Thorns Everywhere',
    'Champions of the Firestorm',
    'The Craft of Conflict',
    'Aggressive',
    'Speculation',
]

r = requests.get("https://rift.events/na/en_US.html")

found_events = []
for event in events:
    if event in r.text:
        found_events.append(event)

if len(found_events):
    events = ', '.join(found_events)
    print(events)
    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(sender, receivers, f"{events}\n\nhttps://rift.events/na/en_US.html")
