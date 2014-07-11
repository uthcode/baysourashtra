import webapp2
from models.person import PersonEntityClass

from utils import thankyou_template, cancel_template

class ThankyouHandler(webapp2.RequestHandler):
  def get(self, email):
    if email:
      person_query = PersonEntityClass.query(PersonEntityClass.email==email)
      if person_query.count():
        person = person_query.fetch()[0]
        person.paid = True
        person.put()
        self.response.write(thankyou_template.render())
      else:
        self.response.write(cancel_template.render())
    else:
      self.response.write(thankyou_template.render())
