import webapp2
from models.person import PersonEntityClassDiwali2014

from utils import thankyou_template, cancel_template

class ThankyouHandler(webapp2.RequestHandler):
  def get(self, email):
    if email:
      person_query = PersonEntityClassDiwali2014.query(PersonEntityClassDiwali2014.email==email)
      if person_query.count():
        person = person_query.fetch()[0]
        person.paid = True
        person.put()
        self.response.write(thankyou_template.render())
      else:
        self.response.write(cancel_template.render())
    else:
      self.response.write(thankyou_template.render())
