import smtplib

import requests


sender = 'tallen@wharton.upenn.edu'
receivers = ['6107217758@vtext.com']

events = [
    'Critical Mass',
    'Inner Maelstrom',
    'Macabre Feast',
    'Melting Point',
    'Thorns Everywhere',
    'Scuttled Dreams',
    'Fortress Defense',
    'Champions of the Firestorm',
    'The Craft of Conflict',
    'Leviathan',
    'Unnatural Spec',
    'Aggressive Colo',
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
