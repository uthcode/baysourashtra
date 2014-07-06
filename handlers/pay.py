import webapp2
from models.person import PersonEntityClass

from utils import pay_template

class PaypalHandler(webapp2.RequestHandler):
  def get(self, email):
    person = PersonEntityClass.query(PersonEntityClass.email==email).fetch()[0]
    values = {
      'name': person.name,
      'spouse': person.spouse,
      'family': person.family,
      'veg': person.veg,
      'nonveg': person.nonveg
    }
    self.response.write(pay_template.render(values))