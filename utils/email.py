from utils import email_template

__author__ = 'skumaran'

from google.appengine.api import mail

message_body_template ="""
Dear %(name)s,

Thank you for registering for the event. Here is your submission details.
Once you pay using our site, your payment record will be updated.

Name: %(name)s
Spouse: %(spouse)s
Family: %(family)s
Adults: %(adults)s
Total Adults Cost: %(total_adults_cost)s
Kids: %(kids)s
Total Kids Cost: %(total_kids_cost)s
Total Food Cost: %(total_food_cost)s

Thank you,
Bay Area Sourashtra Picnic Organizers
"""

def send_email(**kwargs):
  message = mail.EmailMessage(sender="Bay Area Sourashtra Group <baysourashtra@baysourashtra.appspotmail.com>",
                              reply_to="sourashtraevents@gmail.com",
                              bcc=["orsenthil+baysourashtra@gmail.com","sourashtraevents@gmail.com"],
                              subject="Thanks for registering for Sourashtra Gathering Diwali 2015!")
  message.to = kwargs['email']
  message.body = message_body_template % kwargs
  message.html = email_template.render(kwargs)
  message.send()

