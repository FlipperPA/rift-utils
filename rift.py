import smtplib

import requests


sender = 'tallen@wharton.upenn.edu'
receivers = ['**********@vtext.com']

events = [
    'Critical Mass',
    'Fear From Freedom',
    'Inner Maelstrom',
    'Macabre Feast',
    'Melting Point',
    'Rude Awakening',
    'Thorns Everywhere',
    'Why So Sad',
    'Boiling Ambition',
    'Scuttled Dreams',
    'Dreams of Blood and Bone',
    'Chilled to the Bone',
    'The Snow Pack',
    'Hunger of the Deep',
    'Fortress Defense',
    'Champions of the Firestorm',
    'The Craft of Conflict',
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
